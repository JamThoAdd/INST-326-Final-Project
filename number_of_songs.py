
def get_number_of_songs():
    """
    returns a list of all of the songs an artist has and what region on the charts
    """
    import csv
    #open the file for Spotify top 2018 songs
    fh = open("top2018.csv")
    info = csv.DictReader(fh)
    songs = []
    playlist = []
    song_count = 0
    user_input = input("type an artist: ")
    for entries in info:
        if user_input == entries['artists']:
            #adds song to artist's song list
            songs.append(entries['name'])
            #adds 1 to the artist"s total songs count
            song_count += 1
    for entries in info:
        if user_input != entries['artists']:
            print("%s had 0 songs in the Spotify Top 100 Chart of 2018" %user_input)
    print(songs)
    print("%s had " %user_input + str(song_count) + " songs in the Spotify Top 100 Chart of 2018")
# THIS IS A TEST USING ASSERT (artist name must be in the data set in order to have info)
    assert user_input not in entries, "artist must be in data set"


if __name__ == "__main__":
    get_number_of_songs()
