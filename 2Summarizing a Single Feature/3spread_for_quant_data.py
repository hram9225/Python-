#Range-difference between the max and min values of a variable
#Interquartile range(IQR) - the difference between the 75th and 25th percentile values
#Variance- the average of the squared distance from each data point to the mean 
#Standard deviation-the sqaure root of the variance
#Mean absolute deviation (MAD)- mean absolute value of the distance between each data point and the mean 


import pandas as pd

movies = pd.read_csv('movies.csv')

# Save the range to range_budget
range_budget = movies.production_budget.max() - movies.production_budget.min()
print('The range of the production budget is ' + str(range_budget))
# Save the interquartile range to iqr_budget
iqr_budget = movies.production_budget.quantile(0.75) - movies.production_budget.quantile(0.25)
print("The IQR for production budget is " + str(iqr_budget))

# Save the variance to var_budget
var_budget = movies.production_budget.var()
print('The variance for production budget is ' + str(var_budget))

# Save the standard deviation to std_budget
std_budget = movies.production_budget.std()
print("The standard deviation for production budget is " + str(std_budget))

# Save the mean absolute deviation to mad_budget
mad_budget = movies.production_budget.mad()
print('The mean absolute deviation for production budget is ' +str(mad_budget))
