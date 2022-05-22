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
    
    #create lists for calcuations
    month = []
    profit = []
    profit_change = []
        
    for row in csvreader:
        month.append(row[0])
        profit.append(row[1])
    
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
print (f"Total Months : " + str(total_months))
print (f"Total: $" +str(total_profit))
print (f"Average Change: $"+str(ave_change))
print (f"Greatest Increase in Profits "+ {month(month_increase)} +"($"+ str(max_increase)+")")
print (f"Greatest Increase in Profits "+ {month(month_decrease)} +"($"+ str(max_decrease)+")")