import pandas as pd # imports the pandas library

# reads the csv file and creates a pandas.dataframe named vgsales
vgsales = pd.read_csv('vgsales.csv')

# Next 5 lines assigns the individual columns to different variables
naTotalSales = vgsales['NA_Sales'].sum()
euTotalSales = vgsales['EU_Sales'].sum()
jpTotalSales = vgsales['JP_Sales'].sum()
globalTotalSales = vgsales['Global_Sales'].sum()
otherTotalSales = vgsales['Other_Sales'].sum()

# # Creates a list that contains the sums of the individual regional sales
# Uses string.format() to store only up to the second decimal place
sumByRegion = [naTotalSales,euTotalSales,jpTotalSales,globalTotalSales,otherTotalSales] 

total = 0 # Initialize and assigns total to 0

print(sum(sumByRegion))

