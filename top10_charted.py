import csv
import sqlite3

"""
NOTE: database is large so when running file, you need to wait a little bit before you can enter artist name.
Artist names must be capitalized (ex: ed sheeran won't return anything but Ed Sheeran will).
Connects with SQL database. Creates a new table called spotify with columns: position, song, artist, streams, and date.
"""

conn = sqlite3.Connection(":memory:")
cursor = conn.cursor()
db_setup = '''CREATE TABLE spotify (
                position INTEGER,
                song TEXT,
                artist TEXT,
                streams INTEGER,
                date TEXT,
                id INTEGER PRIMARY KEY UNIQUE
                )'''
cursor.execute(db_setup)

"""
sp_query is a query that will insert a row into the table using data from the csv that contains spotify's daily song rankings worldwide.
From the csv file, it will read each row of data, specifically obtaining the position, song, artist, streams, and date.
The row of data will be inserted into the database and saved (committed) until all the rows are inserted into the database.
"""

sp_query = '''INSERT INTO spotify(position, song, artist, streams, date)
                  VALUES (?, ?, ?, ?, ?)'''

with open('data.csv') as handle:
    info = csv.reader(handle)
    for row in info:
        position = row[0]
        song = row[1]
        artist = row[2]
        streams = row[3]
        date = row[5]
        cursor.execute(sp_query, (position, song, artist, streams, date))
        conn.commit()

"""
The user will be able to search by entering the name of an artist. If they enter exit, the loop will break.
If the user does not enter (exit), then a query will be performed.
Using a select statement, it looks for matches in the database using the user's input, or artist's name, as well as any songs positioned above 11.
It will select the song, position, number of streams, and dates from the spotify database.
The results will be ordered by the position the song came on the charts, followed by the number of streams, then by dates.
This will ensure that the user will see the songs charted 10 and above in descending order.
"""
while True:
    search = input('Enter an artist name: ')
    if search == 'exit':
        break

    else:
        artist_query = cursor.execute('''SELECT song, position, streams, date FROM spotify
                                         WHERE artist=? AND position < 11
                                         ORDER BY position, streams, date''',
                                         (search,)).fetchall()

        for n, result in enumerate(artist_query,1):
            song = result[0]
            position = result[1]
            streams = result[2]
            date = result[3]
            print("{0}. {1}, {2} ({3} streams on {4})".format(n, song, position, streams, date))

"""
Above, the results will be enumerated and returned numbered with a format [song, position, (# streams on date)].
This will show the user all of the times that the song by that artist has appeared on the charts.
"""
