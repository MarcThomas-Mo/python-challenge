import os
import csv
from statistics import mean

csvpath = os.path.join('budget_data.csv')

# Set variables to 0 
total_months = 0
net_total = 0
last_month_revenue = 0
revenue_change = 0
revenue_change_list = []

with open(csvpath, 'r', newline="") as csvfile:
    budget_data = csv.reader(csvfile, delimiter=",")

    csv_header = next(budget_data)
 
    for row in budget_data:

        # calculate total months
        total_months = total_months + 1

        # calculates net total 
        net_total = net_total + float(row[1])

        # calculates average change
        # Find difference each month, put in list
        # find sum then div by total in list 
        # Should get -2315.12 acco
        revenue_change = float(row[1]) - last_month_revenue
        last_month_revenue = float(row[1])
        revenue_change_list.append(revenue_change)
        total_changes = (sum(revenue_change_list[1:86])) # skips 0 to leave out first number
        average_change = total_changes / 85 # I KNOW THERE IS PROBABLY A BETTER WAY... BUT I DON'T KNOW
        average_change = round(average_change, 2)
        #print(sum(revenue_change_list))

        # calculates greatest increase
        # Loop through each profit/loss
        # place each value in list
        # find max of list

        # calculates greatest decrease


# summary table
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average  Change: ${average_change}")
# print(f"Greatest Increase in Profits: {}")
# print(f"Greatest Decrease in Profits: {}")