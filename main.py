import pandas as pd # imports the pandas library
from IPython.display import display
import matplotlib.pyplot as plt

# reads the csv file and creates a pandas.dataframe named vgsales
vgsales = pd.read_csv('vgsales.csv')
print(type(vgsales))
# Next 5 lines assigns the sum of each regional sale
naTotalSales = vgsales['NA_Sales'].sum()
euTotalSales = vgsales['EU_Sales'].sum()
jpTotalSales = vgsales['JP_Sales'].sum()
globalTotalSales = vgsales['Global_Sales'].sum()
otherTotalSales = vgsales['Other_Sales'].sum()

<<<<<<< HEAD
# Next 5 lines assigns the individual columns to different variables
naTotalSales = vgsales['NA_Sales'].sum()
euTotalSales = vgsales['EU_Sales'].sum()
jpTotalSales = vgsales['JP_Sales'].sum()
globalTotalSales = vgsales['Global_Sales'].sum()
otherTotalSales = vgsales['Other_Sales'].sum()

# # Creates a list that contains the sums of the individual regional sales
# Uses string.format() to store only up to the second decimal place
<<<<<<< HEAD
sumByRegion = [NA_sales.sum(), JP_sales.sum(),EU_sales.sum(),Other_sales.sum(),Global_sales.sum()] 

total = 0 # Initialize and assigns total to 0

for i in sumByRegion:
    total+=i

    
print(total)
=======
sumByRegion = [naTotalSales,euTotalSales,jpTotalSales,globalTotalSales,otherTotalSales] 

total = 0 # Initialize and assigns total to 0

print(sum(sumByRegion))
>>>>>>> refs/remotes/origin/main
=======
x_values = ['N.A','E.U','JP','Global', 'Other']
y_values = [round(naTotalSales,2),round(euTotalSales,2),
            round(jpTotalSales,2),round(globalTotalSales,2),
            round(otherTotalSales,2)]

color = ['lightblue', 'blue', 'purple', 'red', 'black']
plt.bar(x_values, y_values, width = 0.5, color = color, align='center')
plt.xlabel("Regions")
plt.ylabel("Total (Millions)")
plt.show()
>>>>>>> 959e52be78f134171c74f8c91ad7cd4857033189

