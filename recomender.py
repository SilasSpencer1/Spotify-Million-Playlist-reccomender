popular_songs = open("popular_songs.txt", "r", encoding='utf-8').readlines()
popular_songs = [i.replace("\n", "") for i in popular_songs]
catalog = open("catalog.txt", "r", encoding='utf-8').readlines()

import time

while True:
    try:
        user_track_name = input("Enter track name: ")
        user_artist_name = input("Enter artist name: ")

        user_track = user_track_name + " /// " + user_artist_name

        if user_track in popular_songs:
            print("This song is not undeground")
        else:
            
            all_tracks_of_interest = []
            for i in catalog:
                if user_track in i:
                    all_tracks_of_interest = all_tracks_of_interest + i.replace("\n", "").split(" @@@ ")[: -1]

            unique_tracks_of_interest = list(set(all_tracks_of_interest))

            unique_tracks_of_interest.remove(user_track)

            unique_tracks_of_interest_count = []

            for i in unique_tracks_of_interest:
                counter = 0
                for j in all_tracks_of_interest:
                    if i == j:
                        counter = counter + 1
                unique_tracks_of_interest_count.append(counter)

            max_frequency = max(unique_tracks_of_interest_count)

            print("Recommendations:")
            for i in range(0, len(unique_tracks_of_interest_count)):
                if unique_tracks_of_interest_count[i] == max_frequency:
                    print(unique_tracks_of_interest[i])


    except:
        print("Track you entered is absent in our database")

    cont = input("Do you want to continue? Y/N: ")

    if cont == "Y":
        continue
    elif cont == "N":
        break
