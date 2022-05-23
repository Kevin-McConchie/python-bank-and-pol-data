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
            
        
for p in candidate_votes:
    vote_percent.append(p/total_votes*100)

    #print(p, vote_percent[p])


#assign dictionary values to list so they can be zipped together
candidates= list(poll_result.items())
candidate_votes=list(poll_result.values())

for p in candidate_votes:
    vote_percent.append(round(p/total_votes*100,3))#--------> only rounding to 1 decimal place
    

#prints list of canditate and their votes (vertical print of dicitionary)
# Zip all three lists together into tuples
result_table = zip(candidate, vote_percent, candidate_votes)


#print(candidate, poll_result[candidate])


## The percentage of votes each candidate won


## The winner of the election based on popular vote.
#vote_max = max(candidate_votes)


#print results
print("Election Results:")
print("-------------------------")
print(f"Total Votes: {(total_votes)}")
print("-------------------------")


print (result_table)


# save the output file path
#output_file = os.path.join("output.csv")

# open the output file, create a header row, and then write the zipped object to the csv
#with open(output_file, "w", newline='') as datafile:
