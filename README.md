# Business Data Analysis

**1.Business Scenario & Problem :**

<p>I work for a video game company. Recently we have seen a decline in sales. I've been 
tasked with finding ways to maximize our sales through targeted marketing. I have a
dataset with a breakdown of sales by region and genre.  <p>

**Potential Questions**
<p>What countries/regions should we focus on? What genre of games should we focus on?<p>

**2. Data Life Cycle** <p> <p>
<img width="865" alt="Screenshot 2025-05-08 at 11 02 49 AM" src="https://github.com/user-attachments/assets/cc387420-afaf-47ab-b3fb-abee130d0892" />



**3. Excel Analysis**
<p>For my excel analysis I created a pivot table that displayed the different regions as columns
and genres as rows. From this we can see how much each genre sold in each region.
Using the SUM function I calculated the total sales per genre across all regions. Using this table I created a bar chart
to display the total sales across all regions. I used the INDEX & MATCH functions to create a new column to display
the most profitable genre in each region.</p>
<p><b>Pivot table:</b></p>
<img width="865" alt="Screenshot 2025-05-08 at 10 51 46 AM" src="https://github.com/user-attachments/assets/610a2cf4-6355-44dd-a8a8-9a9f8725619c" />

<p><b>Bar Graph using Excel:</b></p>
<img width="865" alt="Screenshot 2025-05-08 at 4 34 06 AM" src="https://github.com/user-attachments/assets/8cd66ce5-5183-4d1b-b0e6-bca1d362cb50" />

**4. Python Analysis**
<p>Using pandas built in method DataFrame.Head() I printed the first 5 rows on to the console. I got the data type for each column using pandas built in method dtypes.
Using pandas method DataFrame.sum() I got the sum of a specific column. In my case I wanted the sum of each regions' sales. 
With this new total I created a new dataframe that contained the 5 regions
as columns and the total sales as a row. Lastly using matplotlib I created a bar graph that shows the total sales
by region. All of this this is shown below. 
</p>
<img width="865" alt="Screenshot 2025-05-08 at 3 48 20 AM" src="https://github.com/user-attachments/assets/a8a30ff3-37b4-42fe-8e80-c8fe0fe72c53" />

<p><b>Bar Graph using matplotlib:</b></p>

<img src="images/pythonBar.png" alt="bar graph" width="865"/>
<b>5. Data Types :</b> 
Text Most of my data types are numeric and quantitative. Since the sales are in decimals, it would be considered
as continous data. My data was pulled from [Kaggle](https://www.kaggle.com/datasets/anandshaw2001/video-game-sales) text

**6. Conclusion** 
Moving forward I would like to explore the corelation between the genres with the most sales and crimes in the region. 
  For this I would need an additional data set and a way to directly compare the two sets. 
<b>Three Things I learned</b>
<p>
  * How git works remotely and the importance of making sure I am only making changes in one place
  <br>* How to use matplotlib to create graphics
  <br>* How to use pandas to manipulate data from a csv file
</p>










