#Bar charts and pie charts are common for visualizing categorical variable data
# use Seaborn to create bar charts ex: countplot()
#use Pandas & matplotlib for creating pie charts  


import codecademylib3
import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd

movies = pd.read_csv('movies.csv')

# Create a bar chart for movie genre 
sns.countplot(x='genre', data=movies)
plt.show()
plt.close()

# Create a pie chart for movie genre
movies.genre.value_counts().plot.pie()
plt.show()
plt.close()
