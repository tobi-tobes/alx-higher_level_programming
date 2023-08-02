$(document).ready(function () {
  $('DIV#add_item').on('click', function () {
    $('UL.my_list').append('<li>Item</li>');
  });

  $('DIV#remove_item').on('click', function () {
    const last = $('UL.my_list').find('li').last();
    last.detach();
  });

  $('DIV#clear_list').on('click', function () {
    $('UL.my_list').empty();
  });
});
