# Python-Challenge

## Analysis of financial data within [budget_data.csv](PyBank/budget_data.csv). 

In this exercise we are working with a csv that contains two columns of data: "Date" and "Profit/Losses."
The data shows the profit/loss over the period ranging from January 2010 - Februrary 2017.

## PyBank

![Revenue](images/analysis.png)

## Objective

* Create a Python script for analyzing the financial records within the csv file and calulated and display the following results:

  * The total number of months in the dataset

  * The net total amount of "Profit/Losses" over the entire period

  * The average of the changes in "Profit/Losses" over the entire period

  * The greatest increase in profits (date and amount) over the entire period

  * The greatest decrease in losses (date and amount) over the entire period

* Print results to the terminal and exported to a text file.

  ```text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)
  ```
## Breaking Down the Code

  * Used import os and import csv to call csv file and created a variable for the csv file path location.

  * Created variable to read in csv file and variables to hold lists for values of "months", "profit_loss", and "revenue_change" 

  * Created variable to read over header in csv file

  * Used For Loop to read through csv file and appended the values in months column to "months" list and values in Profit/Loss to "profit_loss" list.

  * Found the total months by using counting the length of list "months" and the net total of revenue by using the sum function on list "profit_loss."

  * Used For Loop to calculate the revenue change and append to reveue_change list

  * Calculated the sum of revenue_change and the how many times there was a revenue change to find the average change using sum and len function on our revenue_change variable/list.

  * Created "0" value to append to the beginning of revenue_change to correctly correlate with the list of months.

  * Zipped months and revenue_change into a dictionary

  * Pulled month for highest revenue change and pulled highest revenue change amount using the max () function and stored in variables.

  * Pulled month for the lowest revenue change and the lowest revenue change amount using min() function.

  * Stored all data results into a single variable "financial_analysis."

  * Printed financial_analysis to terminal

  * Createed output path for generating txt file

  * Exported the financial_analysis results to a text file using text writer function ("w", ".write")


