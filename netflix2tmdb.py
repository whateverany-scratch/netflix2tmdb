#!/usr/bin/python3
import dotenv
import os
import pandas
import tmdbsimple

dotenv.load_dotenv()
# Initialize TMDb API
tmdbsimple.API_KEY = os.getenv('TMDB_API_KEY')

# Read Netflix CSV
df = pandas.read_csv('netflix_watch_history.csv')

# Prepare a list to store the results
results = []

# For each title in the CSV, search TMDb
for index, row in df.iterrows():
    title = row['Title']
    
    # Search for the movie in TMDb
    search = tmdbsimple.Search()
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
output_df = pandas.DataFrame(results)
output_df.to_csv('tmdb_watch_history.csv', index=False)
