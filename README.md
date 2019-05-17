INST326 Final Project 
By James Addai, Intisar Muhammad, Kameil Williams, Jessica Tang

# `Spotify Data Analysis`

## Description and Purpose
Our chosen dataset contains information about Spotify's Top 200 Songs Worldwide, which includes data from January 1st, 2017 to January 1st, 2018 in 53 countries. Using this dataset and our project tool, users will be able to analyze data about the artists, songs, chart positions, and regions. We also chose to use another dataset that contains the Top 100 songs of 2018 on Spotify. This dataset is interesting because it includes different aspects of the song including tempo, acoustics, danceability, key, energy, etc.

The purpose of this tool is to allow users to analyze the Spotify charts and use these specs to their liking. This can also introduce them to new songs or artists that they may like.

## What It Does
This tool allows users to:

1. get_artist_tracks
    - Search an artist name. This will return a full list of their songs that appear on the Spotify charts.
2. chart_facts
    - Analyze Top 2018 Spotify charts that show the artists with most presence, songs with the fastest tempo, and songs that have the most danceability.
3. number_of_songs
    - Search an artist name. This will return how many songs they have on the Top 100 list of 2018, as well as a list of those songs.
4. top10_charted
    - Imports data into an SQL database. Allows user to perform a search query using an artist name. This will return all the songs by that artist that charted position 10 and above, how many streams they have and the date it charted in descending order.

## Important Notes
Before you begin, please make sure you have Python3 installed on your system. Then, install the two datasets below in order to run our code properly:

1. https://www.kaggle.com/edumucelli/spotifys-worldwide-daily-song-ranking
2. Download the Top2018 csv file from this repository.

`Note:` The file for step 1 is extremely big. Make sure you have enough space on your system before downloading.
        When running code that uses file 1 (data.csv), it will take several seconds before you will be able to input because it is a **big** file. Please wait a few seconds for it to go through everything!
