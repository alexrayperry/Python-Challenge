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
    months = list(csvreader)
    total_months = len(months)

    #Print Total Months to terminal
    print(f"Total Months: " + str(total_months))
    
# Read through rows (need to complete looo)
    #for row in csvreader:


# Lists to Store data (notsure if needed)
#months = []
#net_total = []


