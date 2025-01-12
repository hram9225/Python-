#nominal variablesare represented by the object data type. String operations like .lower() are not possible on object columns
#Nominal variables are also represented by the string data type. However, Pandas usually guesses object rather than string, so if you want a column to be a string, you will likely have to
#explicitly tell pandas to make it a string. This is most important if you want to do string manipulations on a column like .lower()

#Ordinal variables should be represented as objects, but pandas often guesses int since they are often encoded as whole numbers.

#Binary variables can be represented as bool, but pandas often guesses int or object data types.

import codecademylib3

# Import pandas with alias
import pandas as pd

# Import dataset as a Pandas dataframe
movies = pd.read_csv("netflix_movies.csv")

# View the first five rows of the dataframe
print(movies.head())

# Print the data types of dataframe 
print(movies.dtypes)

# Add the variables you plan to change to this list
change = ['title', 'rating']

# Change the title variable to a "string"
movies['title'] = movies['title'].astype('string') 


# Change any other variables
movies['rating'] = movies['rating'].astype("string")

# Print the data types again
print(movies.dtypes)
