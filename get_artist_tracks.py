
import csv

def get_artist_tracks():
    """
    Allows user to search for an artist
    If entry in data matches the inputed artist, appends song to a list
    Returns a list of all of the songs an artist has on the charts
    """
    fh = open("data.csv")
    info = csv.DictReader(fh)
    #prompt user for an artist name
    user_input = input("type an artist: ")
    songs = []
    for entries in info:
        if user_input in entries['Artist'].lower():
            song_entry = entries['Track Name']
            if song_entry not in songs:
                # add songs that aren't in the song list so you only get unique values
                songs.append(song_entry)
    #print the list of songs from an artist
    print(songs)
if __name__ == "__main__":
    get_artist_tracks()
