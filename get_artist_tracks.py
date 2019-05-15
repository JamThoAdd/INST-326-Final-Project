def get_artist_tracks():
    """
    returns a list of all of the songs an artist has and what region on the charts
    """
    import csv
    fh = open("data.csv")
    info = csv.DictReader(fh)
    user_input = input("type an artist: ")
    songs = []
    for entries in info:
        if user_input in entries['Artist']:
            song_entry = entries['Track Name']
            if song_entry not in songs:
                songs.append(song_entry)
                print(songs)
get_artist_tracks()
