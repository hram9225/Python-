#non-binary categorical variables: has more than two options 

import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import codecademylib3

students = pd.read_csv('students.csv')

#create the box-plot to assess association between test scores and the students fathers jobs 
sns.boxplot(data=students, x='Fjob', y='G3')
plt.show()

print('Most of the data overlaps, however, it is worth noting that students with fathers who are teachers have higher G# scores than students whose father works in a different profession.')

