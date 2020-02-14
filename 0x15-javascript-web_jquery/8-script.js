$(function () {
  $.get(
    'https://swapi.co/api/films/?format=json',
    function(data, textStatus) {
      $.each(data.results, function(index, name) {
        $("ul#list_movies").append($("<li></li>").text(name.title));
      });
    },
    "json"
  )

});
