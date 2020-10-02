#First set modules
import os
import csv

#Set path for CSV file
#Currently not working when I don't set the directory like this... fix this
csvpath = os.path.join('/Users','juliasqueri','Desktop','python_challenge','PyPoll','Resources','election_data.csv')
filepath = os.path.join('/Users','juliasqueri','Desktop','python_challenge','PyPoll','ElectionText.txt')

candidate_dic = {}
total_votes = 0
candidates = []


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
        
        total_votes += 1
        
        candidate = (row[2])

        if candidate in candidate_dic:
            candidate_dic[candidate]+=1
        else:
            candidate_dic[candidate]=1


with open(filepath, mode='w') as txtfile:
    print("Election Results")
    txtfile.write("Election Results\n")
    print("-------------")
    txtfile.write("---------------\n")
    total_votes = (f"Total Votes:  {total_votes}\n")
    print(total_votes)
    txtfile.write(total_votes)
    for candidate in candidate_dic:
        value = candidate_dic[candidate]
        percent = vote_percentage(candidate_dic, candidate)
        result = (f"{candidate}: {percent}% ({value})\n")
        print(result)
        txtfile.write(result)

    for key,value in candidate_dic.items():
        if value == max(candidate_dic.values()):
            winner = (f"Winner: {key}")
            print(winner)
            txtfile.write(winner)









