print("Financial Analysis")
print("------------------------")

import os 
import csv

csvpath = os.path.join('budget_data.csv')

months = []
profit_loss = []
#Hold Revenue Change Values through Each Months
revenue_change = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

# Read over Header
    csv_header = next(csvreader)

    for row in csvreader:

        months.append(row[0])

        profit_loss.append(int(row[1]))

    total_months = len(months)
    #print(f"Total Months: {str(total_months)}")

    net_total = sum(profit_loss)
    #print(f"Total: ${str(net_total)}")

    for i in range(1,len(profit_loss)):
        revenue_change.append(profit_loss[i] -profit_loss[i-1])

    revenue_change_sum = sum(revenue_change)
    revenue_change_count = len(revenue_change)

    average_change = round(revenue_change_sum / revenue_change_count, 2)

    #print(f"Average Change: ${str(average_change)}")

start = 0
revenue_change.insert(0,start)

dict_zip = dict(zip(months, revenue_change))

max_month_key = max(dict_zip, key=dict_zip.get)

max_change = max(revenue_change)

#print(f"Greatest Increase in Profits: {str(max_month_key)} (${str(max_change)})")


min_month_key = min(dict_zip, key=dict_zip.get)

min_change = min(revenue_change)

#print(f"Greatest Decrease in Profits: {str(min_month_key)} (${str(min_change)})")

financial_analysis = (
    "Financial Analysis\n"
    "------------------------\n"
    f"Total Months: {str(total_months)}\n"
    f"Total: ${str(net_total)}\n"
    f"Average Change: ${str(average_change)}\n"
    f"Greatest Increase in Profits: {str(max_month_key)} (${str(max_change)})\n"
    f"Greatest Decrease in Profits: {str(min_month_key)} (${str(min_change)})\n")

print(financial_analysis, end="")


    #for date in months:
        #print(date)

    #for net in profit_loss:
        #print(net)

    
    #Calculate Total Months
    #data = list(csvreader)
    #total_months = len(data)

    #Print Total Months to terminal
    #print(f"Total Months: {str(total_months)}")

    #for row in csvreader:
       #net_total = sum(int(row[1]))
       
      # print(f"Total: {str(net_total)}")