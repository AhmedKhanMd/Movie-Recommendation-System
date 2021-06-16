# This project was implemented as part of my coursera course 

import requests_with_caching
import json

def get_movies_from_tastedive(movie): # return a dictionary consisting of 5 related movie titles for the corresponding movieTitle.
    
    di = {"type":"movies", "limit":5, "q":movie}
    
    results = requests_with_caching.get('https://tastedive.com/api/similar', params = di)
    
    data = results.json()
    
    return data
    
def extract_movie_titles(resultsFromTastedive): #extracting the movie title from the dictionary obtained by get_movies_from_tastedive
    
    movieTitles = []
    
    for i in resultsFromTastedive['Similar']['Results']:
        movieTitles.append(i['Name'])
        
    return movieTitles

def get_related_titles(movieTitles): # returns 5 related movie titles for every input in movieTitles list
    
    resultingList = []
    
    for movieTitle in movieTitles:
        
        relatedMoviesData = get_movies_from_tastedive(movieTitle)
        
        relatedMovies = extract_movie_titles(relatedMoviesData)
        
        for i in relatedMovies:
            
            if i not in resultingList: # In order to avoid duplicat titles in resulting list
                
                resultingList.append(i)
                
    return resultingList

def get_movie_data(movieTitle): # getting additional information for the given movie through OMDB api
    
    di = {"t": movieTitle, "r": "json"}
    
    results = requests_with_caching.get("http://www.omdbapi.com/", params = di)
    
    return results.json()

def get_movie_rating(movieInfo): # returning rotten tomatoes rating for the corresponding movie title.
    
    for i in movieInfo['Ratings']:
        
        if i['Source'] == 'Rotten Tomatoes':
       
            return int(i['Value'][:-1])

    return 0

def get_sorted_recommendations(movieTitles):
    
    relatedTitles = get_related_titles(movieTitles)
    
    moviesAndRating = {}
    
    for i in relatedTitles:
        
        moviesAndRating[i] = get_movie_rating(get_movie_data(i))
        
    
    # sorting recommendations according to the highest rating given by rotten tomatoes
    
    sortedList = [movie[0] for movie in sorted(moviesAndRating.items(),key = lambda x: (x[1], x[0]), reverse = True)] 
    
    return sortedList
