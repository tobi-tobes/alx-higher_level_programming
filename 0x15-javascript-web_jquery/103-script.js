$(document).ready(function () {
  $('INPUT#btn_translate').on('click', function () {
    const language = $('INPUT#language_code').val();
    const hello = $('DIV#hello');
    const url = 'https://hellosalut.stefanbohacek.dev/';
    $.post(url,
      {
        lang: language
      },
      function (data, status) {
        hello.text(data.hello);
      });
  });

  $('INPUT#language_code').keydown(function (e) {
    if (e.keyCode === 13) {
      const language = $('INPUT#language_code').val();
      const hello = $('DIV#hello');
      const url = 'https://hellosalut.stefanbohacek.dev/';
      $.post(url,
        {
          lang: language
        },
        function (data, status) {
          hello.text(data.hello);
        });
    }
  });
});
