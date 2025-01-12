#Univariate summarries-exploring each variable individually 
#Perform initial investigation on data sets using EDA (Exploratory Data Analysis) to get a fell of what you're working with 

import codecademylib3
import pandas as pd

movies = pd.read_csv('movies.csv')

# Print the first 5 rows 
print(movies.head())

# Print the summary statistics for all columns
print(movies.describe(include='all'))

print('Mean, standard deivaition, and percentiles are good for describing quantitative variables. COunt and frequency are better for describing categorical variables.')
