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
def average(profit_loss):
    length = len(profit_loss)
    total = 0
    for number in profit_loss:
        total += number
    return total / length

    #Count total number of months
    

    #Calculate net total amount of Profit/Loss
    
    #Calcuate average of changes in Profit/Loss

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

    
#months.count(row[0])

#print(months.count)

#print("Average is" + str(average(profit_loss)))

#print(f"Total months: {total_months}")
#print(f"Total Profit: {total_profit}")
#print(f"Average change: {av_change}")
#print(f"Maximum:{max(total_profit)}")