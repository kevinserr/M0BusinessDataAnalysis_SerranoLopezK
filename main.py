import pandas as pd # imports the pandas library
from IPython.display import display
import matplotlib.pyplot as plt

# reads the csv file and creates a pandas.dataframe named vgsales
vgsales = pd.read_csv('data/vgsales.csv')

# Next 5 lines assigns the sum of each regional sale
naTotalSales = vgsales['NA_Sales'].sum()
euTotalSales = vgsales['EU_Sales'].sum()
jpTotalSales = vgsales['JP_Sales'].sum()
globalTotalSales = vgsales['Global_Sales'].sum()
otherTotalSales = vgsales['Other_Sales'].sum()

x_values = ['N.A','E.U','JP', 'Other']
y_values = [round(naTotalSales,2),round(euTotalSales,2),
            round(jpTotalSales,2),round(otherTotalSales,2)]

color = ['lightblue', 'blue', 'purple', 'red', 'black']
plt.bar(x_values, y_values, width = 0.5, color = color, align='center')
plt.xlabel("Regions")
plt.ylabel("Total (Millions)")
plt.show()
