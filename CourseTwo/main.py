import pandas as pd

data_csv = pd.read_csv("./percent-bachelors-degrees-women-usa.csv")
# The .head() method returns the first n rows of the DataFrame, 
# where n is the number you specify
print(data_csv.head()) # first 5 rows
print(data_csv.head(20)) # first 20 rows

print(data_csv.tail(20)) # last 20 rows
print(data_csv.info()) # information about the structure of a DataFrame

#print(data_csv.drop()) # drop all the rows of the data frame which contains NA
print(data_csv.fillna("NULL")) # fill missing values in a DataFrame
print(data_csv.drop_duplicates()) #remove duplicate rows from a DataFrame

print(data_csv.iloc[10]) # select rows or columns of a DataFrame by integer position

# Creating the DataFrame
df = pd.DataFrame({'Weight': [45, 88, 56, 15, 71],
                   'Name': ['Sam', 'Andrea', 'Alex', 'Robin', 'Kia'],
                   'Age': [14, 25, 55, 8, 21]})
 
# Create the index
index_ = ['Row_1', 'Row_2', 'Row_3', 'Row_4', 'Row_5']
 
# Set the index
df.index = index_
 
# Corrected selection using loc for a specific cell
# loc -> location - used to access a subset of a DataFrame based on a boolean selection
print(df.loc['Row_2'])
print(df.loc['Row_2', 'Name'])
print(df.loc[:, ['Weight']])
print(df.loc['Row_1'])