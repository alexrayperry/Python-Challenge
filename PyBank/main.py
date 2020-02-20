print("Financial Analysis")
print("------------------------")

import os 
import csv

csvpath = os.path.join('budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

# Read over Header
    csv_header = next(csvreader)
    
    #Calculate Total Months
    data = list(csvreader)
    total_months = len(data)

    #Print Total Months to terminal
    print(f"Total Months: {str(total_months)}")

    for row in csvreader:
       net_total = sum(int(row[1]))
       
       print(f"Total: {str(net_total)}")