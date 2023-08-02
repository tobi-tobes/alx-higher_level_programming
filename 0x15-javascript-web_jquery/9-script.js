$(document).ready(function () {
  const $hello = $('DIV#hello');

  $.ajax({
    type: 'GET',
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    success: function (greeting) {
      $hello.text(greeting.hello);
    }
  });
});
