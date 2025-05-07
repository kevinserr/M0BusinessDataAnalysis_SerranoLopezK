import pandas as pd # imports the pandas library

# reads the csv files and stores it creates a pands.dataframe named vgsales
vgsales = pd.read_csv('vgsales.csv')

# Next 5 lines assigns the individual columns to different variables
NA_sales = vgsales['NA_Sales']
JP_sales = vgsales['JP_Sales']
EU_sales = vgsales['EU_Sales']
Other_sales = vgsales['Other_Sales']
Global_sales = vgsales['Global_Sales']

# Creates a list that contains the sums of the individual region sales
# Using string.format() to store only upto the second decimal place
sumByRegion = ["{:.2f}".format(NA_sales.sum()),"{:.2f}".format(JP_sales.sum()),
               "{:.2f}".format(EU_sales.sum()),"{:.2f}".format(Other_sales.sum()),
               "{:.2f}".format(Global_sales.sum())] 
total = 0 # Initialize and assigns total to 0
# for loop to find the total sum of all regional sales
for i in sumByRegion:
    # converts the string i into a float and then an int in order to compute
    total+= int(float(i))
print(total)

