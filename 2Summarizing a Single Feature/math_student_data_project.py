# Load libraries
import pandas as pd
import numpy as np
import codecademylib3
import matplotlib.pyplot as plt
import seaborn as sns

# Import data
students = pd.read_csv('students.csv')

# Print first few rows of data
print(students.head())
# Print summary statistics for all columns
print(students.describe(include='all'))

# Calculate mean
mean_math_grade = students.math_grade.mean()
print('The mean for the set of math grades is ' + str(mean_math_grade))

# Calculate median
med_math_grade = students.math_grade.median()
print('The median for the set of math grades is ' +str(med_math_grade))
# Calculate mode
mode_math_grade = students.math_grade.mode()
print('The mode for the set of math grades is ' + str(mode_math_grade))

# Calculate range
range_m_grade = students.math_grade.max() - students.math_grade.min()
print('The range for the set of math grades is ' + str(range_m_grade))

# Calculate standard deviation
std_math_grade = students.math_grade.std()
print('The standard deiviation for math grades is ' + str(std_math_grade))
# Calculate MAD
mad_math_grade = students.math_grade.mad()
print('The MAD for math grades is ' + str(mad_math_grade))

# Create a histogram of math grades
sns.histplot(x='math_grade', data=students)
plt.show()
plt.clf()

# Create a box plot of math grades
sns.boxplot(x='math_grade', data=students)
plt.show()
plt.clf()

# Calculate number of students with mothers in each job category
mother_job_counts = students.Mjob.value_counts()
print(mother_job_counts)

# Calculate proportion of students with mothers in each job category
prop_mom_jobs = students.Mjob.value_counts(normalize=True)
print(prop_mom_jobs)
# Create bar chart of Mjob
sns.countplot(x='Mjob', data=students)
plt.show()
plt.clf()

# Create pie chart of Mjob
students.Mjob.value_counts().plot.pie()
plt.show()
