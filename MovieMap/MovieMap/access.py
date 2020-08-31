"""
Methods for accessing the TMDB API
"""

import requests

def getMovie(id):
    "Returns a movie from the TMDB API given a list of movies"
    movies = requests.get('https://api.themoviedb.org/3/movie/'+ id +'?api_key=f3dacf3ab59a006d7aa0aef9a3eaffc5&language=en-US')
    return movies.status_code