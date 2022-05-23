#python-challenge PyPoll code

#import os and csv modules
import os
import csv

election_data = os.path.join("Resources","election_data.csv")

#open and read csv file
with open (election_data, newline="") as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")
    
    #No header row 
    next (csvreader, None)
    
    
    #lists & dictionaries
    
    poll_result ={}
    candidates=[]
    vote_percent=[]
    candidate_votes=[]
    total_votes=0
    
    for row in csvreader:
        candidate = row[2]
        
        #calculation of votes by candidate
        if candidate in poll_result:
            poll_result[candidate] +=1
        else:
           poll_result[candidate] = 1
            
        ## Calculation of total number of votes cast
        total_votes +=1

for key, value in candidate_votes.items():
    candidates.append(key)
    candidate.append(value)
    


#prints list of canditate and their votes
for candidate in poll_result:
    print(candidate, poll_result[candidate])
## A complete list of candidates who received votes

## The percentage of votes each candidate won



for p in candidate_votes:
    vote_percent.append(p/total_votes*100)
   
    #print(p, vote_percent[p])



## The total number of votes each candidate won


## The winner of the election based on popular vote.
#vote_max = max(candidate_votes)

#get winner using Counter's most_common() method.

#print results
print("Election Results:")
print("-------------------------")
print(f"Total Votes: {(total_votes)}")
print("-------------------------")
