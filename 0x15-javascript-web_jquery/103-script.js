// Script that fetches and prints how to say “Hello” depending on the language
$(document).ready(function () {
  $('#btn_translate').click(function () {
    translateHello();
  });

  $('#language_code').keypress(function (event) {
    if (event.keyCode === 13) {
      translateHello();
    }
  });

  function translateHello () {
    const languageCode = $('#language_code').val();
    const apiUrl = `https://www.fourtonfish.com/hellosalut/hello/${languageCode}`;

    $.get(apiUrl, function (data) {
      $('#hello').text(data.hello);
    });
  }
});
