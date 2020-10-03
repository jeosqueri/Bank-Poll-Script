#First set modules
import os
import csv

#Set path for CSV file
csvpath = os.path.join('/Users','juliasqueri','Desktop','python_challenge','PyPoll','Resources','election_data.csv')
#Set path for creating text file
filepath = os.path.join('/Users','juliasqueri','Desktop','python_challenge','PyPoll','Analysis','ElectionText.txt')

#Create empty dictionary to hold candidate names as keys and votes as values
candidate_dic = {}
#Define total votes variable and set to 0
total_votes = 0
candidates = []

#Define vote percentage as a function to call to calculate what % of the vote each candidate won
def vote_percentage(dictionary, s):
    sum = 0
    for key in dictionary:
        sum += dictionary[key]
        percentage = '{0:.2f}'.format(float(dictionary[s])/float(sum)*100)
    return percentage

#Open CSV file
with open(csvpath, mode = 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #Skip header using next function
    next(csvreader)
    for row in csvreader:
        
        #Add 1 to votes
        total_votes += 1
        #Define candidate as being in row 2
        candidate = (row[2])

        #Add candidate name as key and the vote they recieved as value to empty dict
        if candidate in candidate_dic:
            candidate_dic[candidate]+=1
        else:
            candidate_dic[candidate]=1


#Create text file and print results to terminal and text file
with open(filepath, mode='w') as txtfile:
    print("Election Results")
    txtfile.write("Election Results\n")
    print("-------------")
    txtfile.write("---------------\n")
    total_votes = (f"Total Votes:  {total_votes}\n")
    print(total_votes)
    txtfile.write(total_votes)
    #Add new for loop to go through candidate dic and return the candidate name, the number of votes they recieved, and the % of votes 
    for candidate in candidate_dic:
        value = candidate_dic[candidate]
        percent = vote_percentage(candidate_dic, candidate)
        result = (f"{candidate}: {percent}% ({value})\n")
        print(result)
        txtfile.write(result)
    #Find max value of votes in dictionary and return the corresponding key to get the winners name
    for key,value in candidate_dic.items():
        if value == max(candidate_dic.values()):
            winner = (f"Winner: {key}")
            print(winner)
            txtfile.write(winner)









