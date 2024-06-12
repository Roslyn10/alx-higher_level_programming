$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    let moviesList = data.results; // Assuming the data structure has a 'results' array
    let movies = moviesList.map(movie => movie.title).join(', '); // Combine titles into a single string
    $('DIV#list_movies').text(movies);
}); 
