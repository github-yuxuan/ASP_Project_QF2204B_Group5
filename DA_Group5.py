# Q3 import the necessary libraries needed
import pandas as pd, matplotlib.pyplot as plt

# Q4 import excel file into a dataframe
rawdata = pd.read_excel('Project_File.xlsx')

unclean_df = rawdata
print(unclean_df)

# Q5
# Checking columns' datatype
print(unclean_df.dtypes)

# Cleaning the columns by removing whitespaces and renaming the first column to "Date"
unclean_df.columns = unclean_df.columns.str.strip()
unclean_df = unclean_df.rename(columns={'' : 'Date'})

# Convert Year-Month dates into actual datetime
unclean_df['Date'] = pd.to_datetime(unclean_df['Date'])
print(unclean_df)

# Replacing missing values
na_df = unclean_df.replace('na', '0', regex= True)
print(na_df)

# Checking column names in na_df before moving it into
# a new storage 'project_df'
print(na_df.dtypes)
project_df = na_df

# Dataframe (cleansed)
print(project_df)

class RegionPeriod :
    def __init__(self, region, period):
        self.region = region
        self.period = period

# loops through the input to select the region and period of time wanted
    def Region(self):
        global region_df, time_period
        if self.region == "europe":
            region_df = project_df[['Date'] & project_df.iloc[ :, 20:30]]
        elif self.region == "asia":
            region_df = project_df[['Date', 'Brunei Darussalam', 'Indonesia', 'Malaysia', 'Philippines', 'Thailand',
                                    'Viet Nam', 'Myanmar', 'Japan', 'Hong Kong', 'China', 'Taiwan',
                                    'Korea, Republic Of', 'India', 'Pakistan', 'Sri Lanka', 'Saudi Arabia', 'Kuwait', 'UAE']]
        elif self.region == "others":
            region_df = project_df[['Date', 'United Kingdom'] & project_df.iloc[ :, 31:35]]
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

RegionPeriod("asia", "4").Region()
final_df = time_period
print(final_df)

# Q6 to 7
#finding the total sum of visitors throughout the 10 years from 1998 to 2007
# and sort by descending order
total_visitor_series = final_df.sum().sort_values(ascending=False)
print(total_visitor_series)

total_visitor_df = pd.DataFrame({"Country" : total_visitor_series.index,
                                "Total Visitor" : total_visitor_series.values})
print(total_visitor_df)

total_top3_country = total_visitor_df[:3]
print(total_top3_country)

#plotting bar chart
ax = total_top3_country.plot.bar(x ='Country', y ='Total Visitor', rot =0)
plt.title("The top 3 countries in Asia throughout 10 years of 1998 to 2007")
plt.xlabel('Country', fontsize=10)
plt.ylabel('Total Visitor', fontsize=10)

#Adjusting the rotation of x value labels and tightens the plot into a smaller size
#to show the xlabels and ylabels
plt.xticks(rotation = 25)
plt.ticklabel_format(axis="y", style='plain')
ax.bar_label(ax.containers[0], label_type='edge', fmt = '%d')
plt.tight_layout()

#displaying the top 3 countries in the bar chart
plt.show()
