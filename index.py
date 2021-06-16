import requests
import json

def get_movies_from_tastedive(movie):
    
    di = {"type":"movies", "limit":5, "q":movie}
    
    results = requests.get('https://tastedive.com/api/similar', params = di)
    
    data = results.json()
    
    return data


print(get_movies_from_tastedive("Black Panther"))
    

