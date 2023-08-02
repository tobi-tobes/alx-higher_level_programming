$('DIV#toggle_header').on('click', function () {
  if ($('DIV#toggle_header').hasClass('green')) {
    $('DIV#toggle_header').removeClass('green');
  } else {
    $('DIV#toggle_header').removeClass('red');
    $('DIV#toggle_header').addClass('green');
  }
});
