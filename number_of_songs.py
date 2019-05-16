
def get_number_of_songs():
    """
    returns a list of all of the songs an artist has and what region on the charts
    """
    import csv
    fh = open("top2018.csv")
    info = csv.DictReader(fh)
    songs = []
    playlist = []
    song_count = 0
    user_input = input("type an artist: ")
    for entries in info:
        if user_input == entries['artists']:
            songs.append(entries['name'])
            song_count += 1
    for entries in info:
        if user_input != entries['artists']:
            print("%s had 0 songs in the Spotify Top 100 Chart of 2018" %user_input)
    print(songs)
    print("%s had " %user_input + str(song_count) + " songs in the Spotify Top 100 Chart of 2018")
get_number_of_songs()
