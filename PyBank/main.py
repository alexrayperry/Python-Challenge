#Call Dependencies
import os 
import csv

#Create csvfile path location
csvpath = os.path.join('budget_data.csv')

#Lists for holding data values
months = []
profit_loss = []
revenue_change = []

#Create csv reader to read in csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #Read over Header
    csv_header = next(csvreader)

    #Read through csvfile and pull columns of data
    for row in csvreader:

        months.append(row[0])

        profit_loss.append(int(row[1]))

    #Store data in variables
    total_months = len(months)

    net_total = sum(profit_loss)

    #Calculate the revenue change between each month and append to revenue_change list
    for i in range(1,len(profit_loss)):
        revenue_change.append(profit_loss[i] -profit_loss[i-1])
    
    #Calculate the sum of revenue change and the how many times there was a revenue change
    revenue_change_sum = sum(revenue_change)
    revenue_change_count = len(revenue_change)

    #Calculate the average change and round to two decimal points
    average_change = round(revenue_change_sum / revenue_change_count, 2)

#Create "0" value to append to the beginning of revenue change to correctly correlate with the list of months.
start = 0
revenue_change.insert(0,start)

#Zip months and revenue_change into a dictionary
dict_zip = dict(zip(months, revenue_change))

#Pull month for highest revenue change and pull highest revenue change and store in variables.
max_month_key = max(dict_zip, key=dict_zip.get)
max_change = max(revenue_change)

#Pull month for the lowest revenue change and the lowest revenue change amount.
min_month_key = min(dict_zip, key=dict_zip.get)
min_change = min(revenue_change)

#Store all data lines in variable
financial_analysis = (
    "Financial Analysis\n"
    "------------------------\n"
    f"Total Months: {str(total_months)}\n"
    f"Total: ${str(net_total)}\n"
    f"Average Change: ${str(average_change)}\n"
    f"Greatest Increase in Profits: {str(max_month_key)} (${str(max_change)})\n"
    f"Greatest Decrease in Profits: {str(min_month_key)} (${str(min_change)})\n")

#Print final data analysis to terminal
print(financial_analysis, end="")

#Create output path for generating txt file
output_file = os.path.join('financial_analysis.txt')

#Print the results to txt file
with open(output_file, "w") as txt_file:
    txt_file.write(financial_analysis)
    