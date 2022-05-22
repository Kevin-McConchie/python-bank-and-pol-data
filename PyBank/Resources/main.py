#python-challenge PyBank code

#import os and csv modules
import os
import csv

budget_data = os.path.join("budget_data.csv")
budget_data = "budget_data.csv"

#open and read csv file
with open (budget_data, newline="") as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")
    
    #Read Head row 
    csvheader= next(csv_file)
    #print(f"Header:{csv_header}")----------> unsure if neeeded
    
    #Find number of months and profit in dataset
    month = []
    profit = []
    
    for row in csvreader:
        month.append(row[0])
        profit.append(row[1])
    
total_months = len(month)
total_profit = sum(profit)
print(str(total_profit))
# The net total amount of "Profit/Losses" over the entire period
# def average(profit):
#     length = len(profit)
#     total = 0.0
#     for number in profit:
#         total += number
#     return total / length
    
# print (average(profit))

# Test your function with the following:
# print(average([1, 5, 9]))
# print(average(range(11)))


# The average of the changes in "Profit/Losses" over the entire period


# The greatest increase in profits (date and amount) over the entire period
#def print_percentages(wrestler_data):

# The greatest decrease in losses (date and amount) over the entire period


    
    
    #Print results
print ("Financial Analysis")
print ("----------------------------")
print(f" Total Months : " + str(total_months))
#print(f"Total: $" +str(profit))