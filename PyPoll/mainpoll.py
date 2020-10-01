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
        
        total_votes.append(row[0])
        
        candidate = (row[2])

        if candidate in candidate_dic:
            candidate_dic[candidate]+=1
        else:
            candidate_dic[candidate]=1


print(candidate_dic)

#vote_percent = []
#for key in candidate_dic:
    #vote_percent = (round(value/total_votes*100,3))
#for key, value in candidate_dic.items():
    #print(" ".join(key) + " {0} %".format(str(round(value/total_votes*100, 2))))
#print(vote_percent)
#Print total number of votes cast
print("Total Votes: " + str(len(total_votes)))

print("Khan: " + str(candidate_dic["Khan"]) + " " + str(vote_percentage(candidate_dic, "Khan")))
print("Khan: " + str(vote_percentage(candidate_dic, "Khan")) + "%" + " " + "(" + str(candidate_dic["Khan"]) + ")")
print("Correy: " + str(vote_percentage(candidate_dic, "Correy")) + "%" + " " + "(" + str(candidate_dic["Correy"]) + ")")
print("Li: " + str(vote_percentage(candidate_dic, "Li")) + "%" + " " + "(" + str(candidate_dic["Li"]) + ")")
print("O'Tooley: " + str(vote_percentage(candidate_dic, "O'Tooley")) + "%" + " " + "(" + str(candidate_dic["O'Tooley"]) + ")")
#print(f"Khan: {vote_percentage(candidate_dic, "Khan")}% ( {candidate_dic["Khan"]} )")
#Call unique function to print list of candidates
#print(unique(candidates))





