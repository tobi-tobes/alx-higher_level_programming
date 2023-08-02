$(function () {
  const $films = $('UL#list_movies');

  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    success: function (films) {
      const results = films.results;
      $.each(results, function (i, film) {
        $films.append('<li>' + film.title + '</li>');
      });
    }
  });
});
