# Business Data Analysis

**1.Business Scenario & Problem :**

<p>I work for a video game company. Recently we have seen a decline in sales. I've been 
tasked with finding ways to maximize our sales through targeted marketing. I have a
dataset with a breakdown of sales by region and genre.  <p>

**Potential Questions**
<p>What countries/regions should we focus on? What genre of games should we focus on?<p>

**2. Data Life Cycle** <p><p>
<img width="865" alt="Screenshot 2025-05-07 at 3 31 42 PM" src="https://github.com/user-attachments/assets/408055db-988f-47d7-b433-16f5e7a455f5" />

**3. Excel Analysis**
<p>For my excel analysis I created a pivot table that displayed the different regions as columns
and genres as rows. From this we can see how much a particular genre sold and in which region it was most successful.
Using sum I calculated the total sales per genre and region. From this table I was able to create a bar chart
showing the number of sales per genre regardless of region.</p>
<p><b>Pivot table:</b></p>
<img width="865" alt="Screenshot 2025-05-07 at 3 59 35 PM" src="https://github.com/user-attachments/assets/4e74b89a-4df7-44cb-bcc7-b1d2afd422cf" />
<p><b>Bar Graph using Excel:</b></p>
<img width="717" alt="Screenshot 2025-05-08 at 4 34 06 AM" src="https://github.com/user-attachments/assets/8cd66ce5-5183-4d1b-b0e6-bca1d362cb50" />

**4. Python Analysis**
<p>For the python analysis I used pandas to open the csv file and turn it into a DataFrame.
With this DataFrame I'm  able to show the total sales per region. Using the mathlib library I was able to generate a bar graph showing
the sales by region. </p>
<img width="865" alt="Screenshot 2025-05-08 at 3 48 20 AM" src="https://github.com/user-attachments/assets/a8a30ff3-37b4-42fe-8e80-c8fe0fe72c53" />

<p><b>Bar Graph using matplotlib:</b></p>

<img src="images/pythonBar.png" alt="bar graph" width="865"/>

**5. Conclusion** 
<p> Moving forward I would like to explore the corelation between the genres with the most sales and crimes in the region. 
  For this I would need an additional data set and a way to directly compare the two sets. </p>
<b>Three Things I learned</b>
<p>
  * Got git works remotely and the importance of making sure I am only making changes in one place
  <br>* How to use matplotlib to create graphics
  <br>* How to use pandas to manipulate data from a csv file
</p>










