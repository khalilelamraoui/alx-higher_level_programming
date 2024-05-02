// script that fetches and lists the title for all movies by
// using this URL: https://swapi-api.hbtn.io/api/films/?format=json
$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data, textStatus) {
    if (textStatus === 'success') {
      for (const movie of data.results) {
        $('#list_movies').append('<li>' + movie.title + '</li>');
      }
    }
  });
});
