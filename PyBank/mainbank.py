#First set modules
import os
import csv

#Set path for CSV file
#Currently not working when I don't set the directory like this... fix this
csvpath = os.path.join('/Users','juliasqueri','Desktop','python_challenge','PyBank','Resources','budget_data_main.csv')

months = []
profit_loss = []

#Define functions
#Calcuate average of changes in Profit/Loss- AVERAGE FORMULA RIGHT, 
# but needs to be calculating the average of the net profit/loss, so need to calculate that first
def average(diff):
    length = len(diff)
    total = 0
    for number in diff:
        total += number
    return total / length


#Open CSV file
with open(csvpath, mode = 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #Skip header using next function
    next(csvreader)
    for row in csvreader:
        
        #Add months to list
        months.append(row[0])

        #Add profit/loss to list
        profit_loss.append(int(row[1]))
    
        #Generate successive differences for profit list
        diff = [profit_loss[i + 1]- profit_loss[i] for i in range(len(profit_loss)-1)]
        
        #Now get average of diff  

    
print("Financial Analysis")
print("------------------------")

#Print amount of total months
print("Total Months:  " + str(len(months)))

#Print net total amount of profit loss
total = sum(profit_loss)

print("Total:  " + str(total))

#Print average change (need to round)
print("Average Change:   " + str(average(diff)))

#Print Greatest Increase in Profits (Need the month and formatting)
print("Greatest Increase in Profits:  " + str(max(diff)))
#Print Greatest Decrease in Profits (Need the month and formatting)
print("Greatest Decrease in Profits:  " + str(min(diff)))