import pandas as pn
import numpy 
import matplotlib.pyplot as plt
import seaborn as sns
df = pn.read_csv("groceryData.csv")
pn.options.display.max_rows = 9999
print("size of dat:",df )

print(df.dtypes)

#data cleaning

print(df['Item Fat Content'].unique())
df['Item Fat Content'] = df ['Item Fat Content'].replace({'LF':'Low Fat','low fat':'Low Fat','reg':'Regular'})
print(df['Item Fat Content'].unique())

#KPI's Requirements

#Total Sales
total_sales = df['Total Sales'].sum()
#Avg Sales
avg_sales = df['Total Sales'].mean()
#No of Items sold
no_of_items_sold =df['Total Sales'].count()
#Avg Rating
avg_rating = df['Rating'].mean()

print(f"Total Sales: ${(total_sales):,.0f}")
print(f"Avg Sales: ${(avg_sales):,.1f}")
print(f"No of Items sold: {(no_of_items_sold):,.0f}")
print(f"Avg Rating : {(avg_rating ):,.1f}")

#Total Sales by Fat Content
Sales_by_Fat = df.groupby('Item Fat Content')['Total Sales'].sum()
plt.pie(Sales_by_Fat, labels = Sales_by_Fat.index, autopct ='%.0f%%', startangle = 90)

plt.title('Sales by Fat Content')
plt.axis('equal')
plt.show()


# Total Sales by Item Type
Sales_by_Type = df.groupby('Item Type')['Total Sales'].sum().sort_values(ascending=False)
plt.figure(figsize=(10,6))
bars = plt.bar(Sales_by_Type.index, Sales_by_Type.values)

plt.xticks(rotation=-90)
plt.xlabel('Item Type')
plt.ylabel('Total Sales')
plt.title('Total Sales by Item Type')

for bar in bars :
   plt.text(bar. get_x() + bar. get_width() / 2, bar. get_height(), f'{bar. get_height():,.0f}', ha ='center', va = 'bottom', fontsize = 8)
plt.tight_layout()
plt.show()

 # Fat Content by Outlet for Total Sales
grouped = df.groupby(['Outlet Location Type', 'Item Fat Content']) ['Total Sales'].sum().unstack()
grouped = grouped [['Regular', 'Low Fat']]
ax = grouped.plot(kind='bar', figsize=(8, 5), title='Outlet Tier by Item Fat Content')
plt.xlabel('Outlet Location Tier')
plt.ylabel('Total Sales')
plt.legend(title='Item Fat Content')
plt.tight_layout()
plt.show()

# Total Sales by Outlet Establishment

sales_by_year = df.groupby('Outlet Establishment Year')['Total Sales'].sum().sort_index()
plt.figure(figsize=(9,5))
plt.plot(sales_by_year.index, sales_by_year.values, marker='o', linestyle='-')
plt.xlabel('Outlet Establishment Year')
plt.ylabel('Total Sales')
plt.title('Outlet Establishment')

for x, y in zip(sales_by_year.index, sales_by_year.values):
    plt.text(x, y, f'{y:,.0f}', ha='center', va='bottom', fontsize=8)

plt.tight_layout()
plt.show()


# Sales by Outlet Size
sales_by_size = df.groupby('Outlet Size') ['Total Sales'].sum()
plt.figure(figsize=(4, 4))
plt.pie(sales_by_size, labels=sales_by_size.index, autopct='%1.1f%%', startangle=90)
plt.title('Outlet Size')
plt.tight_layout()
plt.show()

# Sales by Outlet Location

sales_by_location = df.groupby('Outlet Location Type') ['Total Sales'].sum().reset_index()
salesby_location = sales_by_location.sort_values('Total Sales', ascending=False)
plt.figure(figsize=(8, 3)) # Smaller height, enough width
ax= sns.barplot(x='Total Sales', y= 'Outlet Location Type', data=sales_by_location)

plt.title('Total Sales by Outlet Location Type')
plt.xlabel('Total Sales')
plt.ylabel('Outlet Location Type')
plt.tight_layout() 
plt.show()
