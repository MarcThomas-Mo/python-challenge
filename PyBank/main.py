import os
import csv


    #file to work from
pybank = os.path.join( "budget_data.csv")

    #lists
change = []
prevdelta = 0
row_counter = 1

    #Read csv file
with open(pybank, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    # skip rows for change calculations
    p = next(csvreader)
    f = next(csvreader)
    #set variable to use for initial change calculation
    prev = (float(f[1]))
    date_list = [(p[0])]
    profit_loss = (float(f[1]))
    #iterate through csv file
    for row in csvreader:
        date_list.append(row[0])
        profit_loss += float(row[1])

        if row_counter >= 1:
            delta = float(row[1]) - prev
            change.append(delta)
            prev= float(row[1])
            row_counter += 1

change_data = zip(date_list, change)
max_increase = 0
max_decrease = 0
for row in change_data:
       
        #find greatest increase and decrease
    if (row[1]) > max_increase:
        max_increase_month =(row[0])
        max_increase = float(row[1])
           # else:
           #     max_increase = max_increase
           #     max_increase_month = max_increase_month
    if (row[1]) < max_decrease:
        max_decrease_month = (row[0])
        max_decrease = float(row[1])
 

dates = len(date_list)
net_profit = (profit_loss)
avg_change = sum(change)/len(change)

    #print out of results
print("Financial Analysis")
print("-------------------")
print(f"Total months: {dates}")
print(f"Total: {net_profit}")
print(f"Average Change: ${round(avg_change,2)}")
print(f"Greatest increase in profits: {max_increase_month} {max_increase}")
print(f"Greatest decrease in profits: {max_decrease_month} {max_decrease}")

#Pybank_Output = open("Pybank_Output.txt", "w") as text_file
with open("Pybank_Output.txt", "w") as textfile:
    textfile.write("Financial Analysis")
    textfile.write("-------------------")
    textfile.write(f"Total months: {dates}")
    textfile.write(f"Total: {net_profit}")
    textfile.write(f"Average Change: ${round(avg_change,2)}")
    textfile.write(f"Greatest decrease in profits: {max_decrease_month} {max_decrease}")
