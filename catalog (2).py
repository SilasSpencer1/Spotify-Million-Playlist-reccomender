import json
import os

names_of_files = os.listdir("data")

all_tracks = open("all_tracks.txt", "w", encoding='utf-8')
catalog = open("catalog.txt", "w", encoding='utf-8')

for i in names_of_files:

    my_file = open('data/' + i)
    data = json.load(my_file)

    for x in data["playlists"]:
        for y in x["tracks"]:
            catalog.write(y['track_name'] + " /// " + y['artist_name'] + " @@@ ")            
            all_tracks.write(y['track_name'] + " /// " + y['artist_name'] + "\n")
        catalog.write("\n")

all_tracks.close()
catalog.close()
    




    













       

    
