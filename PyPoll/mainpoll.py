#First set modules
import os
import csv

#Set path for CSV file
#Currently not working when I don't set the directory like this... fix this
csvpath = os.path.join('/Users','juliasqueri','Desktop','python_challenge','PyPoll','Resources','election_data.csv')

#total_votes = []
#candidates = []

#Create unique name function for generating list of candidate names
#def unique(candidates):
    #unique_list = []
    
    #unique_candidates = set(candidates)

    #for candidates in unique_candidates:
        #unique_list.append(candidates)

    #return unique_list
candidate_dic = {}
total_votes = []
candidates = []

#Open CSV file
with open(csvpath, mode = 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #Skip header using next function
    next(csvreader)
    for row in csvreader:
        
        total_votes.append(row[0])
        
        candidate = (row[2])

        if candidate in candidate_dic:
            candidate_dic[candidate]+=1
        else:
            candidate_dic[candidate]=1


print(candidate_dic)

#Print total number of votes cast
print("Total Votes: " + str(len(total_votes)))

#Call unique function to print list of candidates
#print(unique(candidates))



