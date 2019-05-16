import csv

def get_artist_tracks():
    """
    Allows user to search for an artist 
    If entry in data matches the inputed artist, appends song to a list
    Returns a list of all of the songs an artist has on the charts
    """
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
