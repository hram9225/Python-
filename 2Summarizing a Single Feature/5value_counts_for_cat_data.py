#categorical variables-frequency table containing the count of each distinct value  .value_counts()

import pandas as pd

movies = pd.read_csv('movies.csv')

# Find the number of movies in each genre and print result 

genre_counts = movies.genre.value_counts()
print(genre_counts)
