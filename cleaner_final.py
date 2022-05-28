import pandas as pd
catalog = open("all_tracks.txt", "r", encoding='utf-8').readlines()
catalog = [i.replace("\n", "") for i in catalog]
frequencies = pd.DataFrame(pd.value_counts(catalog))
popular_songs = frequencies[frequencies[0] > 100].index
popular_songs_file = open("popular_songs.txt", "w", encoding='utf-8')
for i in popular_songs:
    popular_songs_file.write(i + "\n")
popular_songs_file.close()

