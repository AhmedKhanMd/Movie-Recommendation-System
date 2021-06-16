import requests
import json

def get_movies_from_tastedive(movie):
    
    di = {"type":"movies", "limit":5, "q":movie}
    
    results = requests_with_caching.get('https://tastedive.com/api/similar', params = di)
    
    data = results.json()
    
    return data

def extract_movie_titles(resultsFromTastedive):
    
    movieTitles = []
    
    for i in resultsFromTastedive['Similar']['Results']:
        movieTitles.append(i['Name'])
        
    return movieTitles

def get_related_titles(movieTitles):
    
    resultingList = []
    
    for movieTitle in movieTitles:
        
        relatedMoviesData = get_movies_from_tastedive(movieTitle)
        
        relatedMovies = extract_movie_titles(relatedMoviesData)
        
        for i in relatedMovies:
            
            if i not in resultingList:
                
                resultingList.append(i)
                
    return resultingList

def get_movie_data(movieTitle):
    
    di = {"t": movieTitle, "r": "json"}
    
    results = requests_with_caching.get("http://www.omdbapi.com/", params = di)
    
    return results.json()

def get_movie_rating(movieInfo):
    
    for i in movieInfo['Ratings']:
        
        if i['Source'] == 'Rotten Tomatoes':
       
            return int(i['Value'][:2])

    return 0

# print(get_related_titles(["Black Panther", "Captain Marvel"]))
# print(get_movie_data("Venom"))
    