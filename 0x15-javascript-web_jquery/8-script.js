$.get('https://swapi-api.hbtn.io/api/films/?format=json', function(data) {
  $.each(data.results, function(implied_iterator, caswellsinfluence) {
    $("UL#list_movies").append('<li>' + caswellsinfluence.title + '</li>')
  })
});