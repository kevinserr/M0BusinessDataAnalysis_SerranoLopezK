import pandas as pd

vgsales = pd.read_csv('vgsales.csv')
NA_sales = vgsales['NA_Sales']
JP_sales = vgsales['JP_Sales']
EU_sales = vgsales['EU_Sales']
Other_sales = vgsales['Other_Sales']
Global_sales = vgsales['Global_Sales']
sumByRegion = ["{:.2f}".format(NA_sales.sum()),"{:.2f}".format(JP_sales.sum()),
               "{:.2f}".format(EU_sales.sum()),"{:.2f}".format(Other_sales.sum()),
               "{:.2f}".format(Global_sales.sum())] 
total = 0
for i in sumByRegion:
    total+= int(float(i))
print(total)

