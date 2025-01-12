#limitations when using correlation or covariance since they measure strngth with linear relationships, not other types like quadratic
import pandas as pd
import matplotlib.pyplot as plt 
import codecademylib3
from scipy.stats import pearsonr

sleep = pd.read_csv('sleep_performance.csv')

# create scatter plot
plt.scatter(sleep.hours_sleep, sleep.performance)
plt.show()

# calculate the correlation for `hours_sleep` and `performance`:
corr_sleep_performance, p = pearsonr(sleep.hours_sleep, sleep.performance)
print(corr_sleep_performance)

