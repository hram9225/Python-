#Also useful to look at proportional values for categorical variables


import pandas as pd

movies = pd.read_csv('movies.csv')

# frind proportion of movies in each genre and print results to console
genre_props = movies.genre.value_counts(normalize=True)
print(genre_props)
