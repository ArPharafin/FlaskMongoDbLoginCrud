$("form[name=signup_form]").submit(function(e) {

  var $form = $(this);
  var $error = $form.find(".error");
  var data = $form.serialize();

  $.ajax({
    url: "/user/signup",
    type: "POST",
    data: data,
    dataType: "json",
    success: function(resp) {
      window.location.href = "/login";
    },
    error: function(resp) {
      $error.text(resp.responseJSON.error).removeClass("error--hidden");
    }
  });

  e.preventDefault();
});

$("form[name=login_form]").submit(function(e) {

  var $form = $(this);
  var $error = $form.find(".error");
  var data = $form.serialize();

  $.ajax({
    url: "/user/login",
    type: "POST",
    data: data,
    dataType: "json",
    success: function (resp) {
      window.location.href = "/main";
    },
    error: function (resp) {
      $error.text(resp.responseJSON.error).removeClass("error--hidden");
    }
  });

  e.preventDefault();
});

  $("form[name=create_form]").submit(function (e) {

    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

    $.ajax({
      url: "/main",
      type: "POST",
      data: data,
      dataType: "json",
      success: function (resp) {
        window.location.href = "/create";
      },
      error: function (resp) {
        $error.text(resp.responseJSON.error).removeClass("error--hidden");
      }
    });

  e.preventDefault();
});
   $("form[name=delete_form]").submit(function (e) {

    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

    $.ajax({
      url: "/main",
      type: "POST",
      data: data,
      dataType: "json",
      success: function (resp) {
        window.location.href = "/delete";
      },
      error: function (resp) {
        $error.text(resp.responseJSON.error).removeClass("error--hidden");
      }
    });

  e.preventDefault();
});
    $("form[name=list_form]").submit(function (e) {

    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

    $.ajax({
      url: "/main",
      type: "POST",
      data: data,
      dataType: "json",
      success: function (resp) {
        window.location.href = "/list";
      },
      error: function (resp) {
        $error.text(resp.responseJSON.error).removeClass("error--hidden");
      }
    });

  e.preventDefault();
});
     $("form[name=update_form]").submit(function (e) {

    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

    $.ajax({
      url: "/main",
      type: "POST",
      data: data,
      dataType: "json",
      success: function (resp) {
        window.location.href = "/update";
      },
      error: function (resp) {
        $error.text(resp.responseJSON.error).removeClass("error--hidden");
      }
    });

  e.preventDefault();
});
      $("form[name=createtion_form]").submit(function (e) {

    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

    $.ajax({
      url: "/main",
      type: "POST",
      data: data,
      dataType: "json",
      success: function (resp) {
        window.location.href = "/main";
      },
      error: function (resp) {
        $error.text(resp.responseJSON.error).removeClass("error--hidden");
      }
    });

  e.preventDefault();
});



