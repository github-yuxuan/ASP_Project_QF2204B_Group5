# Q3 import the necessary libraries needed
import pandas as pd, numpy as np, matplotlib.pyplot as plt, openpyxl

# Q4 import excel file into a dataframe
rawdata = pd.read_excel('Project_File.xlsx')

project_df = rawdata
print(project_df)

# Q5
# Cleaning the columns by removing whitespaces and renaming the first column to "Date"
project_df.columns = project_df.columns.str.strip()
project_df = project_df.rename(columns={'' : 'Date'})
print(project_df)

# Convert Year-Month dates to an actual datetime
project_df['Date'] = pd.to_datetime(project_df['Date'])

print(project_df.columns)
class RegionPeriod :
    def __init__(self, region, period):
        self.region = region
        self.period = period

# loops through the input to select the region and period of time wanted
    def Region(self):
        global region_df, time_period
        if self.region == "europe":
            region_df = project_df[["Date", "United Kingdom", "France", "Germany", "Italy", "Netherlands", "Greece", "Belgium & Luxembourg", "Switzerland",
                            "Austria", "Scandinavia", "CIS & Eastern Europe"]]
        elif self.region == "asia":
            region_df = project_df[['Date', 'Brunei Darussalam', 'Indonesia', 'Malaysia', 'Philippines','Thailand', 'Viet Nam', 'Myanmar', 'Japan', 'Hong Kong', 'China',
                            'Taiwan', 'Korea, Republic Of', 'India', 'Pakistan', 'Sri Lanka', 'Saudi Arabia', 'Kuwait', 'UAE']]
        elif self.region == "others":
            region_df = project_df[['Date', 'USA', 'Canada','Australia', 'New Zealand', 'Africa']]
        else:
            print('End')

        # print(time_period)
        if self.period == "1":
            time_period = region_df[region_df['Date'].between('1978-01-01', '1987-12-31')]
        elif self.period == "2":
            time_period = region_df[region_df['Date'].between('1988-01-01', '1997-12-31')]
        elif self.period == "3":
            time_period = region_df[region_df['Date'].between('1998-01-01', '2007-12-31')]
        elif self.period == "4":
            time_period = region_df[region_df['Date'].between('2008-01-01', '2018-12-31')]
        else:
            print("End")

# asks for input of region and period of time wanted





# Q6
#Finding the specified data for computation
def mean(project_df):
    mean = sum(project_df)/len(project_df)
    return mean

#Split into different column
Country: ["Brunei Darussalam", "Indonesia", "Malaysia", "Philippines", "Thailand", "VietNam", "Myanmar", "Japan",
            "Hong Kong", "China", "Taiwan", "Korea, Republic Of", "India", "Pakistan", "Sri Lanka", "Saudi Arabia",
            "Kuwait", "UAE", "United Kingdom", "Germany", "France", "Italy", "Netherlands", "Greece", "Belgium & Luxembourg",
            "Switzerland", "Austria", "Scandinavia", "CIS & Eastern Europe", "USA", "Canada", "Australia", "New Zealand",
            "Africa"]
project_df =['Date'].str.split(separator, maxsplit)
print(project_df)
