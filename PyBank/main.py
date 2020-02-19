print("Financial Analysis")

import os 
import csv

csvpath = os.path.join('budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

# Reader Header Row first (Not sure if needed)
    csv_header = next(csvreader)
    print(f"Header: {csv_header}")

# Read through rows (need to complete looo)
    for row in csvreader:
        if 

# Lists to Store data (notsure if needed)
months = []
net_total = []


