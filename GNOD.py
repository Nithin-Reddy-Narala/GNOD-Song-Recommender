import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
from sklearn import cluster, datasets
from sklearn.preprocessing import StandardScaler
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from random import randint
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

top_100_songs = pd.read_csv('./top_100_songs.csv')

after_clustering = pd.read_csv('all_top_songs_after_clustering.csv')

all_top_songs = pd.read_csv('all_top_songs.csv')

cid = input('Please input your Spotify Client ID:')
cs_id = input('Please input your Spotify Secret ID:')
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=cid,
                                                           client_secret=cs_id))
                                                           
kmeans = pickle.load(open('kmean.pkl','rb'))
scaler = pickle.load(open('standard.pkl','rb'))


def audio_features(song, artist):
    search = artist + ' - '+ song
    features = sp.audio_features(sp.search(q=search, limit=1)["tracks"]["items"][0]['uri'])[0]
    return features

def songs (data=top_100_songs):
    
    song =  str(input("search songs you are intrested: ").lower())
    artist =  str(input("search artist you are intrested: ").lower())
    search = sp.search(q=song, type='track')
    check = search["tracks"]["total"] 

    while check == 0:
        print("Song does not exists, try another")
        song =  str(input("search songs you are intrested: ").lower())
        artist =  str(input("search artist you are intrested: ").lower())
        search = sp.search(q=song, type='track')
        check = search["tracks"]["total"]

    if ((top_100_songs[(top_100_songs['title'] == song) & (top_100_songs['artist'] == artist)].count()[0] > 0)):
        rand_number = randint(0,len(top_100_songs))
        print("I would recommend you to listen: \"", top_100_songs['title'][rand_number], "\" by", top_100_songs['artist'][rand_number])
    else:       
        feature = audio_features(song,artist)
        new_song = pd.DataFrame([feature])
        new_song = new_song.drop(['type','id','uri','track_href','analysis_url','duration_ms','time_signature'],axis=1)
        new_scaler = scaler.transform(new_song)
        new_clusters = kmeans.predict(new_scaler)
        cluster_final = after_clustering[after_clustering['cluster'] == list(new_clusters)[0]]
        rand_number1 = randint(0,len(after_clustering))
        print("I would recommend you to listen: \"",after_clustering['song_title'][rand_number1], "\" by", after_clustering['artist'][rand_number1])
    return
songs() 