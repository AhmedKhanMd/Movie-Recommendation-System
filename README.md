# Movie-Recommendation-System
A movie recommendation system built using python by combining and processing data that comes from Taste-Dive API and OMDB API.

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Contact](#contact)


## General Information
- When the user provides a movie name as input:
1. Tastedive API is used to get related movie titles(default limit which I have set is 10).
2. Then OMDB API is used to get movie rating for these movie titles.
3. The output will be related movie titles in sorted order according to the Rotten Tomatoe rating.


## Technologies Used
- python - version 3.8
- Tastedive API
- OMDB API

## Setup

1. Install python on your computer(ignore if you already have).
2. Create your account on OMDB and Tastedive and get your own API keys.  
3. clone this repository  
      - Use this command on desired location of your computer.    
      - git clone https://github.com/AhmedKhanMd/Movie-Recommendation-System.git
4. Run the file using command: python index.py 

## Usage

- I did this project as part of my coursera assignment, So I didn't have to generate api keys and also I have used request_with_caching module which was provided by coursera itself
- So If you want to use this:
  - You have to follow setup instructions.
  - Replace requests_with_caching at all the places with requests.


## Project Status
Project is: completed.

## Contact
feel free to contact me!
mak181354@gmail.com.
