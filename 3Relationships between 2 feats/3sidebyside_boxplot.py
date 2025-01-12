#Side-by-side box plots are useful for visualizing mean and median differences. Can help determine if the differences are large or small. 
import pandas as pd
import codecademylib3
import matplotlib.pyplot as plt 
import seaborn as sns

students = pd.read_csv('students.csv')

#create the boxplot here:
sns.boxplot(data = students, x = 'address', y = 'G3')
plt.show()
