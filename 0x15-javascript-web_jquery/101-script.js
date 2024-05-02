// script that adds, removes and clears LI elements from a list when the user clicks
$(document).ready(function () {
  // Add item to the list
  $('#add_item').click(function () {
    $('UL.my_list').append('<li>Item</li>');
  });

  // Remove last item from the list
  $('#remove_item').click(function () {
    $('UL.my_list li:last-child').remove();
  });

  // Clear the entire list
  $('#clear_list').click(function () {
    $('UL.my_list').empty();
  });
});
