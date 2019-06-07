import os
import csv

    #setting counters
votes = 0
khan = 0
correy = 0
li = 0
otooley = 0

    #file to work from
pypoll = os.path.join("election_data.csv")

    #Read CSV file
with open(pypoll, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter =",")
    #skip header row
    next(csvreader)
    #iterate through data
    for row in csvreader:
        votes += 1
        if (row[2]) == "Khan":
            khan += 1
        elif (row[2]) == "Correy":
            correy += 1
        elif (row[2]) == "Li":
            li += 1
        elif (row[2]) == "O'Tooley":
            otooley += 1

    #percent calculations
khanpercent = "{:.3%}".format(khan / votes)
correypercent = "{:.3%}".format(correy / votes)
lipercent = "{:.3%}".format(li / votes)
otooleypercent = "{:.3%}".format(otooley / votes)

if khanpercent > correypercent and khanpercent > lipercent and khanpercent> otooleypercent:
    winner = "Khan"
elif correypercent > khanpercent and correypercent > lipercent and correypercent > otooleypercent:
    winner = "Correy"
elif lipercent > khanpercent and lipercent > correypercent and lipercent > otooleypercent:
    winner = "Li"
elif otooleypercent > khanpercent and otooleypercent > correypercent and otooleypercent > lipercent:
    winner = "O'Tooley"
print("ELECTION RESULTS")
print("-----------------")
print(f"Total Votes: {votes}")
print("-----------------")
print(f"Khan:  {khanpercent} ({khan})")
print(f"Correy:  {correypercent} ({correy})")
print(f"Li: {lipercent} ({li})")
print(f"O'Tooley: {otooleypercent} ({otooley})")
print("------------------")
print(f"Winner: {winner}")

#output text file
with open("Pypoll_Output.txt", "w") as textfile:
    textfile.write("ELECTION RESULTS")
    textfile.write("-----------------")
    textfile.write(f"Total Votes: {votes}")
    textfile.write("-----------------")
    textfile.write(f"Khan:  {khanpercent} ({khan})")
    textfile.write(f"Correy:  {correypercent} ({correy})")
    textfile.write(f"Li: {lipercent} ({li})")
    textfile.write(f"O'Tooley: {otooleypercent} ({otooley})")
    textfile.write("------------------")
    textfile.write(f"Winner: {winner}")
