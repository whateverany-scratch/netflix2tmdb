#!/usr/bin/python3
import pandas as pd
import tmdbsimple as tmdb

# Initialize TMDb API
tmdb.API_KEY = 'YOUR_TMDB_API_KEY'  # Get your API key from https://www.themoviedb.org

# Read Netflix CSV
df = pd.read_csv('netflix_watch_history.csv')

# Prepare a list to store the results
results = []

# For each title in the CSV, search TMDb
for index, row in df.iterrows():
    title = row['Title']
    
    # Search for the movie in TMDb
    search = tmdb.Search()
    response = search.movie(query=title)
    
    if search.results:
        movie_id = search.results[0]['id']  # Get the first result's ID
        movie_title = search.results[0]['title']
        release_date = search.results[0]['release_date']
        
        # Append the relevant data
        results.append({
            'Title': movie_title,
            'TMDb ID': movie_id,
            'Release Date': release_date,
            'Watched Date': row['Date']
        })

# Create a DataFrame from the results and export to CSV
output_df = pd.DataFrame(results)
output_df.to_csv('tmdb_watch_history.csv', index=False)

print("Conversion completed! File saved as 'tmdb_watch_history.csv'.")


