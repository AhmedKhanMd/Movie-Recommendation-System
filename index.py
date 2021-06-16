import requests
import json

def get_movies_from_tastedive(movie):
    
    di = {"type":"movies", "limit":5, "q":movie}
    
    results = requests.get('https://tastedive.com/api/similar', params = di)
    
    data = results.json()
    
    return data

def extract_movie_titles(resultsFromTastedive):
    
    movieTitles = []
    
    for i in resultsFromTastedive['Similar']['Results']:
        movieTitles.append(i['Name'])
        
    return movieTitles

print(extract_movie_titles(get_movies_from_tastedive("Black Panther")))
    

