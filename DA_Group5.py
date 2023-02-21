# Q3 import the necessary libraries needed
import pandas as pd, numpy as np, matplotlib.pyplot as plt, openpyxl

# Q4 import excel file into a dataframe
rawdata = pd.read_excel('Project_File.xlsx')

project_df = rawdata
print(project_df)

# Q5
# Checking columns' datatype (w/o cleansing)
print(project_df.dtypes)

# Cleaning the columns by removing whitespaces and renaming the first column to "Date"
project_df.columns = project_df.columns.str.strip()
project_df = project_df.rename(columns={'' : 'Date'})

# Convert Year-Month dates into actual datetime
project_df['Date'] = pd.to_datetime(project_df['Date'])
print(project_df)

# Finding missing values


# Replacing missing values


# Checking column names (with cleansing)


# Dataframe (cleansed)

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

# Q6
RegionPeriod("asia", "2").Region()
final_df = time_period
print(final_df)

# Q7
plt.bar(final_df['Region'], final_df['Date'])
plt.show();

project_df = country[['country_model', 'Date']].plot(kind='bar', title = "Top 3 country", figsize=(10,10), legend=True, fontsize=12)
plt.show();

project_df = country['Date'].plot(kind='hist', title ="Range in Date", figsize=(10,10), legend=True, fontsize=12)
plt.show();