#continuous variables: store as float so we can store decimals 
#discrete: store as int 
#If a number is stored as the wrong data type, can still change it using .astype() function 
#can be used to convert numerical data types such as int32, int64, float32, float64, object, string, & bool
#some data types require all values to be filled in (cannot convert between a float and int if there any null values)

import codecademylib3

# Import pandas with alias
import pandas as pd

# Import dataset as a Pandas dataframe
movies = pd.read_csv("netflix_movies.csv")

# View the first five rows of the dataframe
print(movies.head())

# Print the data types
print(movies.dtypes)

movies['cast_count'] = movies['cast_count'].fillna(0).astype("int64")

# Fill in the missing cast_count values with 0
movies['cast_count'].fillna(0, inplace = True)

# Change the type of the cast_count column

# Check the data types of the columns again. 
print(movies.dtypes)

