import codecademylib3

# Import pandas with alias
import pandas as pd

# Read in the census dataframe
census = pd.read_csv('census_data.csv', index_col=0)

print(census.head())

print(census.dtypes)
print(census['birth_year'].unique())

census['birth_year'] = census['birth_year'].replace(['missing'], 1967)

print(census['birth_year'].unique())

census['birth_year'] = census['birth_year'].astype('int64')
print(census.dtypes)

print(census['birth_year'].mean())

census['higher_tax'] = pd.Categorical(census['higher_tax'], ['strongly disagree', 'disagree', 'neutral', 'agree', 'strongly agree'], ordered=True)

print(census['higher_tax'].unique())

census['higher_tax'] = census['higher_tax'].cat.codes
print(census['higher_tax'].median())

census = pd.get_dummies(census, columns = ['marital_status'])
print(census.head())



# Create a new variable called marital_codes by Label Encoding the marital_status variable. This could help the Census team use machine learning to predict if a respondent thinks the wealthy should pay higher taxes based on their marital status.

# Create a new variable called age_group, which groups respondents based on their birth year. The groups should be in five-year increments, e.g., 25-30, 31-35, etc. Then label encode the age_group variable to assist the Census team in the event they would like to use machine learning to predict if a respondent thinks the wealthy should pay higher taxes based on their age group.
