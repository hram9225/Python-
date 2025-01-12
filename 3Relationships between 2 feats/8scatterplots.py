#

import pandas as pd
import matplotlib.pyplot as plt 
import codecademylib3

housing = pd.read_csv('housing_sample.csv')

print(housing.head())

#create scatter plot

plt.scatter(x = housing.beds, y = housing.sqfeet)
plt.xlabel('Number of Bedrooms)')
plt.ylabel('Area (Square Feet)')
plt.show()
