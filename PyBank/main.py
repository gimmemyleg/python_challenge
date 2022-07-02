# importing modules that allow to handle and use file pathing
import os
import csv
from statistics import mean

# to access data easier later, new list variables are generated
Date = []
Profit_loss = []
Change = []

# create path to the csv file, and one for txt file for analysis.txt
filepath = os.path.join("Resources", "budget_data.csv")
resultpath = os.path.join("analysis", "analysis.txt")
# print(filepath) <- This was used to print filepath as a reference

# open the file using the file path above, read original file
with open(filepath, 'r', encoding = "utf-8") as file :

    # create the reader object(file stream)
    csvReader = csv.reader(file, delimiter = ",")
    # grab header (skips header)
    csvheader = next(csvReader)
    # read each row of data from the file
    for row in csvReader:

        # each row, row[0] will be added to Date, and row[1] will be added to Profit_loss
        Date.append(row[0])
        Profit_loss.append(int(row[1]))

    # loop that runs a set number of times based on the values of Proft_loss
    # Each difference of Profit_loss[2] and Profit_loss[1] will be saved at Change list
    for i in range(len(Profit_loss)-1):
        Change.append(int(Profit_loss[i+1]) - int(Profit_loss[i]))   

# define maximum change of profit/loss and minimum change of profit/loss 
# and average change of profit/loss
maxchange = max(Change)
minchange = min(Change)
avgchange = round(mean(Change),2)

# total month will be equal to count of all Date inside Date list
total_month = len(Date)
# total Profit and loss will be sum of list Profit_loss
total = sum(Profit_loss)

# finding index for maxchange nad minchange to get Date when this particular change occurs.
index_bigmonth = Change.index(maxchange)
index_smallmonth = Change.index(minchange)
bigmonth = Date[index_bigmonth+1]
smallmonth = Date[index_smallmonth+1]
# print out output to terminal
output = (
    f"\nFinancial Analysis\n"
    f"-------------------------\n"
    f"Total Month: {total_month}\n"
    f"Total: ${total}\n"
    f"Average Change: ${avgchange}\n"
    f"Greatest Increase in Profits: {bigmonth} (${maxchange})\n"
    f"Greatest Decrease in Profits: {smallmonth} (${minchange})\n"
)
print(output)

# open the output file and write analysis.txt with result
with open(resultpath ,"w") as outfile:
    outfile.writelines(output)