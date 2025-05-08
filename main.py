import pandas as pd # imports the pandas library
import matplotlib.pyplot as plt # import lib for graphing

# reads the csv file and creates a pandas.dataframe named vgsales
vgsales = pd.read_csv('data/vgsales.csv')

# set_option is used to display all columns
pd.set_option('display.max_columns', None)

print("First 5 Rows:")
print(vgsales.head(5)) # shows only the first 5 rows
print('Data Types for All Columns: \n')
print(vgsales.head(0).dtypes) # displays the dtypes for only the first row

# Next 5 lines assigns the sum of each regional sale using sum()
naTotalSales = vgsales['NA_Sales'].sum()
euTotalSales = vgsales['EU_Sales'].sum()
jpTotalSales = vgsales['JP_Sales'].sum()
otherTotalSales = vgsales['Other_Sales'].sum()

# next 2 lines defines the x & y values for my bar graph
x_values = ['N.A','E.U','JP','Other']
y_values = [round(naTotalSales,2),round(euTotalSales,2),
            round(jpTotalSales,2),round(otherTotalSales,2)]

# creates new dataframe to display onto the console
df = pd.DataFrame({'N.A': [naTotalSales],
                   'E.U': [euTotalSales],
                   'JP': [jpTotalSales],
                   'Other': [otherTotalSales]},
                   index=['Total Sales:'])

print('Data Frame with region and their total sales','\n')
print(df) # displays dataframe on to the console

color = ['lightblue', 'blue', 'purple', 'red'] # defines the colors for the bar graph
plt.bar(x_values, y_values, width = 0.5, color = color, align='center')
# next 3 lines add titles 
plt.xlabel("Regions")
plt.ylabel("Total (Millions)")
plt.title('Total Sales by Region')
plt.show() # displays the bar graph
