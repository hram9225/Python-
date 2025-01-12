import numpy as np
import pandas as pd
from scipy.stats import pearsonr, chi2_contingency
import matplotlib.pyplot as plt
import seaborn as sns

import codecademylib3
np.set_printoptions(suppress=True, precision = 2)

nba = pd.read_csv('./nba_games.csv')

# Subset Data to 2010 Season, 2014 Season
nba_2010 = nba[nba.year_id == 2010]
nba_2014 = nba[nba.year_id == 2014]

print(nba_2010.head())
print(nba_2014.head())

#create 2 series that represent points each team has scored in their games 
knicks_pts_10 = nba_2010.pts[nba.fran_id=='Knicks']
nets_pts_10 = nba_2010.pts[nba.fran_id=='Nets']

#calculate difference between the teams average points scored 
average_knicks = np.mean(knicks_pts_10)
average_nets = np.mean(nets_pts_10)
diff_means_2010 = average_knicks - average_nets
print(diff_means_2010)

#create a set of overlapping histograms 
plt.hist(knicks_pts_10, alpha=0.8, normed = True, label='knicks')
plt.hist(nets_pts_10, alpha=0.8, normed = True, label='nets')
plt.legend()
plt.title("2010 Season")
plt.show()

#repeat the previous steps for the 2014 data
# Create series for points scored by each team in 2014
knicks_pts_14 = nba_2014.pts[nba_2014.fran_id == 'Knicks']
nets_pts_14 = nba_2014.pts[nba_2014.fran_id == 'Nets']

# Calculate the mean points for each team in 2014
knicks_mean_score_14 = np.mean(knicks_pts_14)
nets_mean_score_14 = np.mean(nets_pts_14)

# Calculate the difference between the two means
diff_means_2014 = knicks_mean_score_14 - nets_mean_score_14
print(diff_means_2014)

# Plot overlapping histograms
plt.clf()  # Clear previous plots
plt.hist(knicks_pts_14, alpha=0.8, normed=True, label='Knicks')
plt.hist(nets_pts_14, alpha=0.8, normed=True, label='Nets')
plt.legend()
plt.title("2014 Season")
plt.show()

#5. generate side-by-side boxplots
# Clear previous plots
plt.clf()

# Generate side-by-side boxplots
sns.boxplot(data=nba_2010, x='fran_id', y='pts')

# Show the plot
plt.show()

#6 calculate a table of frequencies that show counts of game_result and game_location
# Calculate the contingency table of frequencies
location_result_freq = pd.crosstab(nba_2010['game_result'], nba_2010['game_location'])

# Print the result
print(location_result_freq)

#7. convert the table of frequencies to a table of proportions 
# Calculate the table of proportions
location_result_proportions = location_result_freq / location_result_freq.sum().sum()

# Print the result
print(location_result_proportions)


#8. calculate expected contingency table and the Chi-Square statistic and print results
from scipy.stats import chi2_contingency

# Calculate the Chi-Square statistic and expected frequencies
chi2, pval, dof, expected = chi2_contingency(location_result_freq)

# Print the expected table and Chi-Square statistic
print("Expected Table:")
print(expected)
print("\nChi-Square Statistic:")
print(chi2)

#9. calculate covariance between forecast and point_diff 
# Calculate the covariance matrix
cov_matrix = np.cov(nba_2010['forecast'], nba_2010['point_diff'])

# Extract the covariance between forecast and point_diff
point_diff_forecast_cov = cov_matrix[0, 1]

# Print the result
print(point_diff_forecast_cov)


#10. calculate correlation betwene forcast and points_diff

from scipy.stats import pearsonr

# Calculate the correlation coefficient
point_diff_forecast_corr, _ = pearsonr(nba_2010['forecast'], nba_2010['point_diff'])

# Print the result
print(point_diff_forecast_corr)

#11. create a scatter plot of forecast(x=axis) and point_diff9y-axis)
# Clear previous plots
plt.clf()

# Generate the scatter plot
plt.scatter(nba_2010['forecast'], nba_2010['point_diff'])

# Label the axes
plt.xlabel('Forecasted Win Probability')
plt.ylabel('Point Differential')

# Show the plot
plt.show()



