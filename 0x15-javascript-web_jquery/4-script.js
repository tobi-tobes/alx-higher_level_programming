$('DIV#toggle_header').on('click', function () {
  if ($('DIV#toggle_header').hasClass('green')) {
    $('DIV#toggle_header').removeClass('green');
    $("DIV#toggle_header").addClass("red");
  } else {
    $('DIV#toggle_header').removeClass('red');
    $('DIV#toggle_header').addClass('green');
  }
});
