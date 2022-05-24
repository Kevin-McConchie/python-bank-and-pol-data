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
    
    #collation of candidate and votes
    for row in csvreader:
        candidate = row[2]
        
        ## Calculation of total number of votes cast
        total_votes +=1
        
        #calculation of votes by candidate
        if candidate in poll_result:
            poll_result[candidate] +=1
        else:
            poll_result[candidate] = 1
            


#assign dictionary values to list so they can be zipped together
candidates= list(poll_result.keys())
candidate_votes=list(poll_result.values())

for p in candidate_votes:
    vote_percent.append('{:.3f}%'.format(p/total_votes*100,3))
    

#print results
print("Election Results:")
print("-------------------------")
print(f"Total Votes: {(total_votes)}")
print("-------------------------")
result_table = zip(candidates, vote_percent, candidate_votes)

#prints list of canditate and their votes (vertical print of dicitionary)
# Zip all three lists together
for i, (candidates, vote_percent, candidate_votes) in enumerate(result_table):
    print(f"{candidates}:  {vote_percent} ({candidate_votes})")



## The winner of the election based on popular vote.

#winner = max(candidate_votes)

# save the output file path
output_path = os.path.join("Analysis", "Election Result.txt")

# open the output file with summary of election results
with open(output_path, 'w', newline='') as textfile:
    
        textfile.writelines(f"Election Results \n------------------------- \nTotal Votes:  {(total_votes)}\n-------------------------\n")
        for entry in result_table:
            textfile.writelines(f"{entry[0]}: {entry[2]}% ({entry[1]})\n")
        
        
    

    
#print results
# print ((result_table))
# print (tuple(result_table))
# print(vote_percent)
# print(candidate_votes)
# print (candidates)
#print(candidate, poll_result[candidate])