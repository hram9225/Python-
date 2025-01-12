#Another way of encoding categorical variables is called One-Hot Encoding (OHE). With OHE, we essentially create a new binary variable for each of the categories within our original variable. 
#This technique is useful when managing nominal variables because it encodes the variable without creating an order among the categories.

import codecademylib3

# Import pandas with alias
import pandas as pd

# Import dataset as a Pandas Dataframe
cereal = pd.read_csv('cereal.csv', index_col=0)

# Show the first five rows of the `cereal` dataframe
print(cereal.head())

# Create a new dataframe with the `mfr` variable One-Hot Encoded
cereal = pd.get_dummies(cereal, columns = ['mfr'])

# Show first five rows of new dataframe
print(cereal.head())
