import pandas as pd # imports the pandas library
from IPython.display import display
import matplotlib.pyplot as plt

# reads the csv file and creates a pandas.dataframe named vgsales
vgsales = pd.read_csv('data/vgsales.csv')
pd.set_option('display.max_columns', None)

print("First 5 Rows:")
print(vgsales.head(5))
print('Data Types for All Columns: \n')
print(vgsales.head(0).dtypes)

# Next 5 lines assigns the sum of each regional sale
naTotalSales = vgsales['NA_Sales'].sum()
euTotalSales = vgsales['EU_Sales'].sum()
jpTotalSales = vgsales['JP_Sales'].sum()
otherTotalSales = vgsales['Other_Sales'].sum()

x_values = ['N.A','E.U','JP','Other']
y_values = [round(naTotalSales,2),round(euTotalSales,2),
            round(jpTotalSales,2),round(otherTotalSales,2)]

df = pd.DataFrame({'N.A': [naTotalSales],
                   'E.U': [euTotalSales],
                   'JP': [jpTotalSales],
                   'Other': [otherTotalSales]},
                   index=['Total Sales:'])

print('Data Frame with region and their total sales','\n')
print(df)

color = ['lightblue', 'blue', 'purple', 'red']
plt.bar(x_values, y_values, width = 0.5, color = color, align='center')
plt.xlabel("Regions")
plt.ylabel("Total (Millions)")
plt.show()
