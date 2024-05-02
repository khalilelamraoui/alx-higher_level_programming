// Script that adds LI to a list when the clicking on the tag DIV#add_item
$('DIV#add_item').click(function () {
  $('UL.my_list').append('<li>Item</li>');
});
