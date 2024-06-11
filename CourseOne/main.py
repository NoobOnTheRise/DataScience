import pandas as pd
import openpyxl

# read a csv file
data_csv = pd.read_csv("./percent-bachelors-degrees-women-usa.csv")
print(data_csv)

# read a txt file
data_txt = pd.read_csv("StudentSchool.txt", header= 0, spe = ',')
print(data_txt)

# read an excel file
data_excel = pd.read_excel("file.xlsx", sheet_name = 'Sheet1')
print(data_excel)

# read from a json
data_json = pd.read_json("./filename.json")
print(data_json)

# read from sql
import sqlite3
connection_db = sqlite3.connect("database_name.db")
query_1 = "SELECT * FROM table_name"
data_sql = pd.read_sql(query_1,connection_db)