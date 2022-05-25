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

#work out percentage of votes per candidate
for p in candidate_votes:
    vote_percent.append('{:.3f}%'.format(p/total_votes*100,3))
    

#print results
print("Election Results:")
print("-------------------------")
print(f"Total Votes: {(total_votes)}")
print("-------------------------")

#prints list of canditate and their votes (vertical print of dicitionary)
# Zip all three lists together
result_table = list(zip(candidates, vote_percent, candidate_votes))

for i, (candidates, vote_percent, candidate_votes) in enumerate(result_table):
    print(f"{candidates}:  {vote_percent} ({candidate_votes})")
print("-------------------------")


#find winner
winner = max(poll_result,key=poll_result.get)
print(winner)

# save the output file path
output_path = os.path.join("Analysis", "Election Result.txt")

# open the output file with summary of election results
with open(output_path, 'w', newline='') as textfile:
    
        textfile.writelines(f"Election Results \n------------------------- \nTotal Votes:  {(total_votes)}\n-------------------------\n")
        for row in result_table:
            textfile.writelines(f"{row[0]}: {row[1]}% ({row[2]})\n")
        textfile.writelines("-------------------------\n")
        textfile.writelines(f"Winner: {winner}\n")
        
    

    
#print results
# print ((result_table))
# print (tuple(result_table))
# print(vote_percent)
#print(candidate_votes)
# print (candidates)
#print(candidate, poll_result[candidate])