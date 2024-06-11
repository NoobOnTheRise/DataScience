import pandas as pd

data_csv = pd.read_csv("./percent-bachelors-degrees-women-usa.csv")
# The .head() method returns the first n rows of the DataFrame, 
# where n is the number you specify
print(data_csv.head()) # first 5 rows
print(data_csv.head(20)) # first 20 rows

