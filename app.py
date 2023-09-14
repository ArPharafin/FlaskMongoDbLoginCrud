from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from pymongo import MongoClient
import bcrypt

app = Flask(__name__)
client = MongoClient()
from bson import ObjectId

app.secret_key = "chastoharmony"
app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017/omerfaruk"

mongo = PyMongo(app)


@app.route('/', methods=['POST', 'GET'])
def homepage():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # MongoDB'ye kayıt ekleme işlemi
        mongo.db.register.insert_one({"email": email, "name": name, "password": hashed_password})

        # Kullanıcıyı /login sayfasına yönlendir
        return redirect(url_for('loginpage'))  # loginpage isimli route'a yönlendir

    return render_template('register.html')




@app.route('/login', methods=['POST', 'GET'])
def loginpage():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = mongo.db.register.find_one({"email": email})

        if user and bcrypt.checkpw(password.encode('utf-8'), user['password']):
            return redirect('/main')
        else:
            return render_template('login.html')

    return render_template('login.html')


@app.route('/main', methods=['POST', 'GET'])
def create_page():
    # create'ye basınca create gitsin
    # delete basınca delete gitsin #ObjectId'ye göre sil
    # update basınca update gitsin
    # list basınca list gitsin
    return render_template('main.html')


@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        ad = request.form.get('ad')  # Corrected from 'name' to 'ad'
        soyad = request.form.get('soyad')  # Corrected from 'email' to 'soyad'
        tckn = request.form.get('tckn')
        sehir = request.form.get('sehir')
        ugurlusayi = request.form.get('ugurlusayi')

        mongo.db.createpagedengelenler.insert_one(
            {"ad": ad, "soyad": soyad, "tckn": tckn, "sehir": sehir, "ugurlusayi": ugurlusayi})
        return render_template('main.html')
    return render_template('create.html')


@app.route('/main', methods=['POST', 'GET'])
def delete_page():
    return render_template('delete.html')


@app.route('/delete', methods=['POST', 'GET'])
def delete():
    if request.method == 'POST':
        user_id = request.form.get('_id')
        mongo.db.createpagedengelenler.delete_one({"_id": ObjectId(user_id)})
        return render_template('main.html')
    return render_template('delete.html')

@app.route('/main', methods=['POST', 'GET'])
def updatePage():
    return render_template('update.html')

@app.route('/update', methods=['POST', 'GET'])
def update():
    if request.method == 'POST':
        _id = request.form.get('_id')
        ad = request.form.get('ad')
        soyad = request.form.get('soyad')
        tckn = request.form.get('tckn')
        sehir = request.form.get('sehir')
        ugurlusayi = request.form.get('ugurlusayi')

        # MongoDB'de belgeyi güncelle
        existing_doc = mongo.db.createpagedengelenler.find_one({"_id": ObjectId(_id)})
        _id = request.form.get('_id')
        # ObjectId dönüşümü
        _id = ObjectId(_id)
        if existing_doc:

            mongo.db.createpagedengelenler.update_one(
                {"_id": ObjectId(_id)},
                {
                    "$set": {
                        "ad": ad,
                        "soyad": soyad,
                        "tckn": tckn,
                        "sehir": sehir,
                        "ugurlusayi": ugurlusayi
                    }
                }
            )
            return "Güncelleme başarılı"

        # Eğer belge bulunamazsa hata mesajı dönebilirsiniz
        return "Belge bulunamadı"

    return render_template('update.html')



@app.route('/main', methods=['POST', 'GET'])
def list_page():
    return render_template('list.html')


@app.route('/list', methods=['POST', 'GET'])
def list():

    documents = mongo.db.createpagedengelenler.find({})


    return render_template("list.html", documents=documents)





if __name__ == '__main__':
    app.run()

# aynı sayfada iki buton oalcak. birincisi kayıt ol ikincisi giriş yap
