# GNOD - Song Recommender based on Spotify API
### Recommending a song based on user-inputter song through unsupervised clustering & song features


This project is a part of Ironhack Data Analytics Full Time Bootcamp course.

## 1. Project Description
* This project has been finished to practice the unsupervised machine learning (clustering) with a wide array of models, as well as working with Spotify API to extract the songs' features - both real time and statically. The project consists of two main data sets:

* Hot100 (400) songs - currently curated pop songs; if the user inputs a title from that list, he/she automatically gets a random song from that list too;

* A database of approx. 12k songs from a variety of Spotify playlists, with their features such as enegry, tempo, danceability included.

* After the user inputs a chosen song's title and artist, the recommender will connect with Spotify API, extract the song's features, run the clustering model to assign the song into one of the available clusters and then choose a random song from the same cluster & provide it back to the user.

## 2. Tools used
* The main technologies used here are Python, Pandas and Spotify API. The data is cleaned & wrangled using Pandas and final databases are exported to .csv files.

## 3. Challenges identified
* The main challenge within the project was to create a somewhat accurate model that could cluster the songs into usable (recommendable) categories. Selecting the right model type and optimizing the parameters took the bulk of the project time.

## 4. How to use & install
* The project is straightforward to install, use & modify:

* Fork & clone the entire repo on your hard-drive
* Run the 'GNOD' notebook or .py script

Nithin Reddy Narala
