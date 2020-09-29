#First set modules
import os
import csv

#Set path for CSV file
csvpath = os.path.join('..','Resources','budget_data_main.csv')

months = []

#Define functions
#def financial_anal(budget_data):
    #date = str(budget_data[0])
    #profit_loss = int(budget_data[1])

    #Count total number of months
    #total_months = count(date)

    #Calculate net total amount of Profit/Loss
    #net_total = 
    #Calcuate average of changes in Profit/Loss


#Open CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #Skip header using next function
    next(csvreader)
    for row in csvreader:
        #Define date and profit/loss inside loop
        #date = row[0]
        #proft_loss = row[1]

        #Add months to list
        months.append(row[0])

    

        #counts = []

        #for i in months:
            #counts[int(months)] = (counts[int(months)] + 1)
            #print(counts)

    
months.count(row[0])

print(months.count(date))


#print(f"Total months: {total_months}")
#print(f"Total Profit: {total_profit}")
#print(f"Average change: {av_change}")
#print(f"Maximum: {max(total_profit)}")
#print(f"Minimum: {min(total_profit)}")



    