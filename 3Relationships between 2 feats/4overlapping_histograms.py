#setting alpha to .5 ensures the histograms are see through 
#normed=True y-axis is a density reather than a frequency
#newest version of matplotlib uses density instead of normed


import numpy as np
import pandas as pd
import codecademylib3
import matplotlib.pyplot as plt 
students = pd.read_csv('students.csv')

scores_urban = students.G3[students.address == 'U']
scores_rural = students.G3[students.address == 'R']

#create the overlapping histograms
plt.hist(scores_urban, color='green', label='urban', normed=True, alpha=0.5)
plt.hist(scores_rural, color='yellow', label='rural', normed=True, alpha=0.5)
plt.legend()
plt.show()
