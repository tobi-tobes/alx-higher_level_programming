$(document).ready(function () {
  const language = $('INPUT#language_code').val();
  const hello = $('DIV#hello');
  const url = 'https://hellosalut.stefanbohacek.dev/';

  $('INPUT#btn_translate').on('click', function () {
    $.post(url,
      {
        lang: language
      },
      function (data, status) {
        hello.text(data.hello);
      });
  });

  $('INPUT#language_code').keydown(function (e) {
    $.post(url,
      {
        lang: language
      },
      function (data, status) {
        hello.text(data.hello);
      });
  });
});
