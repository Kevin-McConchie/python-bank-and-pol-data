#python-challenge PyBank code

#import os and csv modules
import os
import csv

budget_data = os.path.join("Resources","budget_data.csv")


#open and read csv file
with open (budget_data, newline="") as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")
    
    #Read Head row 
    csvheader= next(csv_file)
    
    
    #create lists for calcuations
    month = []
    profit = []
    profit_change = []
    
    #adds months and profit to lists   
    for row in csvreader:
        month.append(row[0])
        profit.append(row[1])
    
    #checks future cell against current and acounts for index starting at 0 and not going beyond last value
    #also accounts for 1 less change as first value doesn't have a change
    for y in range(len(profit)-1):
        profit_change.append(int(profit[y+1])-int(profit[y]))
            

#find total months
total_months = len(month)

# The net total amount of "Profit/Losses" over the entire period
total_profit = sum(int(x) for x in profit)

# The average of the changes in "Profit/Losses" over the entire period
sum_profit_change = sum(profit_change)
ave_change = round((sum_profit_change) / (total_months-1),2)


# The greatest increase in profits (date and amount) over the entire period
max_increase = max(profit_change)
month_increase = profit_change.index(max(profit_change))+1

# The greatest decrease in losses (date and amount) over the entire period
max_decrease = min(profit_change)
month_decrease = profit_change.index(min(profit_change))+1
    
    
#Print results
print ("Financial Analysis")
print ("----------------------------")
print (f"Total Months : {str(total_months)}")
print (f"Total: ${(total_profit)}")
print (f"Average Change: ${str(ave_change)}")
print (f"Greatest Increase in Profits {month[month_increase]} ${max_increase}")
print (f"Greatest Increase in Profits {month[month_decrease]} ${max_decrease}")

# Specify the file to write to
output_path = os.path.join("Analysis", "analysis.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'a', newline='') as f:

    # Write Analysis in Analysis/analysis.txt
    f.write("Financial Analysis\n")
    f.write("----------------------------\n")
    f.write(f"Total Months : {str(total_months)}\n")
    f.write(f"Total: ${(total_profit)}\n")
    f.write(f"Average Change: ${str(ave_change)}\n")
    f.write(f"Greatest Increase in Profits {month[month_increase]} ${max_increase}\n")
    f.write(f"Greatest Increase in Profits {month[month_decrease]} ${max_decrease}\n")


