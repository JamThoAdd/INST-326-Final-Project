def chart_facts():
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    from scipy.stats import pearsonr
    df=pd.read_csv('top2018.csv')
    largest_presence = df['artists'].value_counts().head(10)
    most_danceable = df[['name','artists','danceability']].sort_values(by='danceability',ascending=False).head(10)
    fastest_songs = df[['name','artists','danceability', 'tempo']].sort_values(by='tempo',ascending=False).head(10)
    print(largest_presence)
    print("As you can see, XXXTENTACION had the biggest presence on Spotify with 6 songs in the top 100")
    print("These are the songs with the fastest tempo", fastest_songs)
    print("These are the most danceable songs on a scale from 0.0-1.0", most_danceable)
if __name__ == "__main__":
    chart_facts()
