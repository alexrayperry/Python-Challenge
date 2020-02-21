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
    print(f"Total Months: {str(total_months)}")

    net_total = sum(profit_loss)
    print(f"Total: ${str(net_total)}")

    for i in range(1,len(profit_loss)):
        revenue_change.append(profit_loss[i] -profit_loss[i-1])

    revenue_change_sum = sum(revenue_change)
    revenue_change_count = len(revenue_change)

    average_change = revenue_change_sum / revenue_change_count

    print(f"Average Change: ${str(average_change)}")


    

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