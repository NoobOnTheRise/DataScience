import pandas as pd

data = pd.DataFrame({
    'Name': ['Anne', ' Karen' , 'John', 'Kevin', 'Sanna' , ' Bob', 'Emily'],
    'Age': [35,30,57,65,25,19,20],
    'Salary': [20000, 60000, 1450000, 1700000, 30000, 10000, 2200000],
    'Department': ['Tech', 'Tech', 'Tech', 'Healthcare', 'Operations', 'Operations', 'Tech']
})

# Ascending - smallest values at the top and values increasing
print(data.sort_values(by = 'Salary'))
print("(-------------------------------)")
print(data.sort_values(by = 'Salary', ascending=True))
print("(-------------------------------)")
print(data.sort_values(by = 'Age', ascending=True))

# Descending
print("(-------------------------------)")
print(data.sort_values(by = 'Salary', ascending=False))


# count the no of people in an department
print("(-------------------------------)")
print(data.groupby('Department').count())
print(data.groupby('Department')['Name'].count())
print(data.groupby('Department')['Salary'].mean()) # average
print(data.groupby('Department')['Salary'].min()) 
print(data.groupby('Department')['Salary'].max()) 

# filtering
print("(-----------------More than 100000--------------)")
print(data[data['Salary'] > 100000])

print("(-----------------Salart Between 100000 and 2000000--------------)")
print(data[(data['Salary'] > 100000) & (data['Salary'] < 2000000)])

print("(-----------------Age etween 20 and 65--------------)")
print(data[data['Age'].isin([20,65])])
