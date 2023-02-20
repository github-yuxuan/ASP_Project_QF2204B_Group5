# Q3 import the necessary libraries needed
import pandas as pd, numpy as np, matplotlib.pyplot as plt, openpyxl

# Q4 import excel file into a dataframe
rawdata = pd.read_excel('Project_File.xlsx')

project_df = rawdata

# Q5
# # Cleaning the columns by removing whitespaces and renaming the first column to "Date"
project_df.columns = project_df.columns.str.strip()
project_df = project_df.rename(columns={'' : 'Date'})

#Convert Year-Month dates to an actual datetime
project_df['Date'] = pd.to_datetime(project_df['Date'])

print(project_df)

project_df.replace('na', 0)

project_dfna = project_df.isnull().sum()
print(project_dfna)