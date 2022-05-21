#python-challenge PyBank code

#import os and csv modules
import os
import csv

#need to fix this####
budget_data = os.path.join("PyBank","Resources", "budget_data.csv")

#open and read csv file
with open (budget_data, newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    
    #Print report header
    print ("Financial Analysis")
    print ("----------------------------")
    
    #Total number of months in dataset
month = True
months = 0

for row in csv_reader:
    if row[0] ==  True:
        months = months+1

        month = True
        
    if month is None:   
        print (months)
    
    #months.append (rows[1])
    
    #print(f" Total Months : " + str(len(months)))
    


# The net total amount of "Profit/Losses" over the entire period
# def average(numbers):
#     length = len(numbers)
#     total = 0.0
#     for number in numbers:
#         total += number
#     return total / length
#

# Test your function with the following:
# print(average([1, 5, 9]))
# print(average(range(11)))


# The average of the changes in "Profit/Losses" over the entire period


# The greatest increase in profits (date and amount) over the entire period
#def print_percentages(wrestler_data):

# The greatest decrease in losses (date and amount) over the entire period

#Read Head row ----------> unsure if neeeded
    #csv_header= next(csv_file)
    #print(f"Header:{csv_header}")