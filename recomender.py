try:
    user_track_name = input("Enter track name: ")
    user_artist_name = input("Enter artist name: ")

    user_track = user_track_name + " /// " + user_artist_name


    catalog = open("catalog.txt", "r", encoding='utf-8').readlines()

    playlists_with_track = []
    for i in catalog:
        if user_track in i:
            this_list_tracks = i.replace("\n", "").split(" @@@ ")
            this_list_tracks = this_list_tracks[:len(this_list_tracks) - 1]
            playlists_with_track.append(this_list_tracks)


    all_tracks_of_interest = []
    for i in playlists_with_track:
        all_tracks_of_interest = all_tracks_of_interest + i
    unique_tracks_of_interest = list(set(all_tracks_of_interest))


    unique_tracks_of_interest.remove(user_track)

    unique_tracks_of_interest_count = []

    for i in unique_tracks_of_interest:
        counter = 0
        for j in playlists_with_track:
            if i in j:
                counter = counter + 1
        unique_tracks_of_interest_count.append(counter)

    max_frequency = max(unique_tracks_of_interest_count)

    print("Recommendations:")
    for i in range(0, len(unique_tracks_of_interest_count)):
        if unique_tracks_of_interest_count[i] == max_frequency:
            print(unique_tracks_of_interest[i])

except:
    print("Track you entered is absent in our database")
