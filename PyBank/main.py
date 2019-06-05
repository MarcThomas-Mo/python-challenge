import os
import csv
from statistics import mean

    #file to work from
pybank = os.path.join( "budget_data.csv")

    #lists
date_list = []
change = []
profit_loss = 0


    #Read csv file
with open(pybank, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader)
    f =next(csvreader)
    prev = (float(f[1]))

    for row in csvreader:
        row_counter = 2
        date_list.append(row[0])
        profit_loss += float(row[1])
        if row_counter > 1:
            prev = float(row[1])-prev
            change.append(prev)
            row_counter += 1
print(change)

dates = len(date_list)
net_profit = (profit_loss)
avg_change = mean(change)
#print out of results
print(f"change list {change}")
print("Financial Analysis")
print("-------------------")
print(f"Total months: {dates}")
print(f"Total: {net_profit}")
print(f"Average Change: ${avg_change}")
#print(f"Greatest increase in profits: {}")
#print(f"Greatest decrease in profits: {}")
