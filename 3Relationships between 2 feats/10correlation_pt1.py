#Pearson Correlation is a scaled form of covariance; measures the strength of a linear relationship but ranges from -1 to +1.
#highly associated variables with a positive linear relationship will have a correlation factor close to 1.
#highly associated variables with a negative linear relationship will have a correlation cloase to -1
#variables that have no assocaition (or linear assocation with a slope of 0) will have correlations close to 0. 
#use pearsonr() from scipy.stats to calculate correlation
#usually correlation larger than 0.3 indicates linear association. larger than 0.6 suggests a strong linear association. 

import pandas as pd
import matplotlib.pyplot as plt 
import codecademylib3
from scipy.stats import pearsonr

housing = pd.read_csv('housing_sample.csv')

# calculate corr_sqfeet_beds and print it out:
corr_sqfeet_beds, p = pearsonr(housing.sqfeet, housing.beds)
print(corr_sqfeet_beds)

# create the scatter plot:
plt.xlabel('Number of beds')
plt.ylabel('Number of sqfeet')
plt.scatter(x = housing.beds, y = housing.sqfeet)
plt.show()
