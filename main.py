import pandas as pd # imports the pandas library

# reads the csv file and creates a pandas.dataframe named vgsales
vgsales = pd.read_csv('vgsales.csv')

# Next 5 lines assigns the individual columns to different variables
NA_sales = vgsales['NA_Sales']
JP_sales = vgsales['JP_Sales']
EU_sales = vgsales['EU_Sales']
Other_sales = vgsales['Other_Sales']
Global_sales = vgsales['Global_Sales']

# Creates a list that contains the sums of the individual regional sales
# Uses string.format() to store only up to the second decimal place
sumByRegion = [NA_sales.sum(), JP_sales.sum(),EU_sales.sum(),Other_sales.sum(),Global_sales.sum()] 

total = 0 # Initialize and assigns total to 0

for i in sumByRegion:
    total+=i

    
print(total)

