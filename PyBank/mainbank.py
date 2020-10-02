#First set modules
import os
import csv

#Set path for CSV file
csvpath = os.path.join('/Users','juliasqueri','Desktop','python_challenge','PyBank','Resources','budget_data_main.csv')
txtpath = os.path.join('/Users','juliasqueri','Desktop','python_challenge','PyBank','BankText.txt')

months = []
#Current profit list
profit_loss = []

#Define average function to call to calculate the average changes in profit/loss over entire period
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

        #Add current profit/loss to list
        profit_loss.append(int(row[1]))
    
        #Generate successive differences for profit list
        diff = [profit_loss[i + 1]- profit_loss[i] for i in range(len(profit_loss)-1)]
        


#month by month results
total_months = len(months)
total_profit_change = sum(profit_loss)
average_change = round(average(diff), 2)
max_change = max(diff)
max_month = months[diff.index(max_change) + 1]
min_change = min(diff)
min_mounth = months[diff.index(min_change) + 1]

with open(txtpath, mode ='w') as txtfile:
    print("Financial Analysis")
    txtfile.write("Financial Analysis\n")
    print("------------------------")
    txtfile.write("------------------------\n")
    #Print amount of total months
    print(f"Total Months:  {total_months}")
    txtfile.write(f"Total Months:  {total_months}\n")
    #Print net total amount of profit loss
    print(f"Total: ${total_profit_change}")
    txtfile.write(f"Total: ${total_profit_change}\n")
    #Print average change
    print(f"Average Change: ${average_change}")
    txtfile.write(f"Average Change: ${average_change}\n")
    #Print Greatest Increase in Profits (Need the month and formatting)
    print(f"Greatest Increase in Profits: {max_month} (${max_change})" )
    txtfile.write(f"Greatest Increase in Profits: {max_month} (${max_change})\n")
    #Print Greatest Decrease in Profits (Need the month and formatting)
    print(f"Greatest Decrease in Profits: {min_mounth} (${min_change})")
    txtfile.write(f"Greatest Decrease in Profits: {min_mounth} (${min_change})\n")