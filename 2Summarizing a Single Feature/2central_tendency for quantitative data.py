#Mean-average value of the variable .mean()
#Median-middle value of the variable when all values have been sorted.  .median()
#Mode-Most frequent value .mode()
#Trimmed mean-mean excluding x percent of the lowest and highest data points. 


import pandas as pd

movies = pd.read_csv('movies.csv')

# Save the mean to mean_budget
mean_budget = movies.production_budget.mean()
print('The mean of the production budget is ' + str(mean_budget))
# Save the median to med_budget
med_budget = movies.production_budget.median()
print('The median of the production budget is ' + str(med_budget))
# Save the mode to mode_budget
mode_budget = movies.production_budget.mode()
print('The mode of the production budget is ' + str(mode_budget))

# Save the trimmed mean to trmean_budget 
#remove 20% of the lowest and highest data points 

from scipy.stats import trim_mean
trmean_budget = trim_mean(movies.production_budget, proportiontocut=0.2)
print('The trimmed mean of the production budget is ' + str(trmean_budget))
