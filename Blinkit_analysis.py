#------------------DATA ANALYSIS PYTHON PROJECT - BLINKIT ANALYSIS--------------------

#-----IMPORT LIBRARIES--------
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

#------SAMPLE DATA--------
df = pd.read_csv(r"C:/Users/DELL/Desktop/Blinkit Analysis/blinkit_data.csv")
print(df.head(20))
print(df.tail(20))

#------SIZE OF DATA--------
print("Size of Data :", df.shape)

#------FIELD INFO----------
print(df.columns)

#------DATA TYPES----------
print(df.dtypes)

#--------------DATA CLEANING---------------
print(df['Item Fat Content'].unique())
df["Item Fat Content"] = df["Item Fat Content"].replace({'LF': 'Low Fat', 
                                                         'low fat': 'Low Fat', 
                                                         'reg': 'Regular'})
print(df['Item Fat Content'].unique())

#---------BUSINESS REQUIREMENTS----------------

#-------KPI's Requirements------------
#Total Sales
total_sales = df['Sales'].sum()

#Average Sales
avg_sales = df['Sales'].mean()

#No. of Items Sold
no_of_items_sold = df['Sales'].count()

#Average Ratings
avg_ratings = df['Rating'].mean()

#Display
print(f"Total Sales: ${total_sales:,.0f}")
print(f"Average Sales: ${avg_sales:,.1f}")
print(f"No of Items Sold: ${no_of_items_sold:,.0f}")
print(f"Average Ratings: ${avg_ratings:,.1f}")

#-------------CHARTS REQUIREMENTS-----------------------

#----------Total Sales by Fat Content------------
sales_by_fat = df.groupby('Item Fat Content')['Sales'].sum()
plt.pie(sales_by_fat, labels = sales_by_fat.index, autopct = '%.1f%%', startangle=90)
plt.title('Sales By Fat Content')
plt.axis('equal')
plt.show()

#------Total Sales by Item Type--------
sales_by_type = df.groupby('Item Type')['Sales'].sum().sort_values(ascending=False)

plt.figure(figsize=(10,6))
bars = plt.bar(sales_by_type.index, sales_by_type.values)
plt.xticks(rotation=-90)
plt.xlabel("Item Type")
plt.ylabel('Total Sales')
plt.title('Total Sales by Item Type')

for bar in bars:
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), 
             f"{bar.get_height():,.0f}", ha='center', va='bottom', fontsize = 8)
plt.tight_layout()
plt.show()

#--------Fast Content by Outlet for Total Sales------
grouped = df.groupby(['Outlet Location Type', 'Item Fat Content'])['Sales'].sum().unstack()
grouped = grouped[['Regular', 'Low Fat']]
ax = grouped.plot(kind='bar', figsize=(8,5), title='Outlet Tier by Item Fat Content')
plt.xlabel('Outlet Location Tier')
plt.ylabel('Total Sales')
plt.legend(title='Item Fat Content')
plt.tight_layout()
plt.show()

#-------Total Sales by Outlet Establishment-----------
sales_by_year = df.groupby('Outlet Establishment Year')['Sales'].sum().sort_index()
plt.figure(figsize=(9,5))
plt.plot(sales_by_year.index, sales_by_year.values, marker = 'o', linestyle='-')
plt.xlabel("Outlet Establishment Year")
plt.ylabel("Total Sales")
plt.title('Outlet Establishment')

for x, y in zip(sales_by_year.index, sales_by_year.values):
    plt.text(x, y, f"{y:,.0f}", ha='center', va='bottom', fontsize=0)
plt.tight_layout()
plt.show()

#--------Sales y Outlet Size------------
sales_by_size = df.groupby('Outlet Size')['Sales'].sum()
plt.figure(figsize=(4,4))
plt.pie(sales_by_size, labels=sales_by_size.index, autopct='%1.1f%%', startangle=90)
plt.title('Outlet Size')
plt.tight_layout()
plt.show()

#-----------Sales by Outlet Location---------------
sales_by_location = df.groupby('Outlet Location Type')['Sales'].sum().reset_index()
sales_by_location = sales_by_location.sort_values('Sales', ascending=False)
plt.figure(figsize=(8,3))
ax = sns.barplot(x='Sales', y='Outlet Location Type', data=sales_by_location)
plt.title("Total Sales by Outlet Location Type")
plt.xlabel('Total Sales')
plt.ylabel('Outlet Location type')
plt.tight_layout()
plt.show()

