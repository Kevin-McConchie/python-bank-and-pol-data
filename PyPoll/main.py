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
    
    
    #create lists for calcuations
    candidates=[]
    candidate_votes ={}
    total_votes=0
    
    for row in csvreader:
        candidate = row[2]
        
        if candidate in candidate_votes:
            candidate_votes[candidate] +=1
        else:
            candidate_votes[candidate] = 1
        total_votes +=1
    
    print(candidate_votes)
    

## The total number of votes cast


## A complete list of candidates who received votes
for candidate in candidate_votes:
    print(candidate, candidate_votes[candidate])

## The percentage of votes each candidate won


## The total number of votes each candidate won


## The winner of the election based on popular vote.
#vote_max = max(candidate_votes)

#get winner using Counter's most_common() method.
