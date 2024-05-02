// script that displays the value of hello from
// this URL: https://hellosalut.stefanbohacek.dev/?lang=fr
$(document).ready(function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data, textStatus) {
    $('DIV#hello').text(data.hello);
  });
});
