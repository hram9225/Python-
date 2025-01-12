import codecademylib3

# Import pandas with alias
import pandas as pd

# Import dataset as a Pandas dataframe
movies = pd.read_csv("netflix_movies.csv")

# View the first five rows of the dataframe
print(movies.head())

# Set the correct value for release_year_variable_type
release_year_variable_type = 'discrete'
print(release_year_variable_type)

# Set the correct value for duration_variable_type
cast_count_variable_type = 'discrete'
print(cast_count_variable_type)

