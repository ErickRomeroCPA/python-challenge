import os
import csv

# path to collect data from the resources folder
budget_data = os.path.join('resources','budget_data.csv')

# counter for total_profit
total_profit = 0

#arrays
month_list = []
profit_list = []
change_list = []
change_list = []
#read in the csv file
with open(budget_data,'r') as csvfile:

    #split data on commas
    csvreader = csv.reader(csvfile,delimiter=',')

    header = next(csvreader)

    #loop through data
    for row in csvreader:
        # assigning values to variables w/ descriptive names
    #finding total months value
        month = row[0]
        month_list.append(month)
        total_months = len(month_list)

    #finding total profit value,greatest increase in and add profit value to profit_list
        profit = int(row[1])
        total_profit = total_profit + profit
        profit_list.append(profit)
        
    #finding avg change value & greatest increase/decrease in profits
    for i in range(len(profit_list) - 1):
        change = int(profit_list[i + 1]) - int(profit_list[i])
        change_list.append(change)
        avg_change = sum(change_list) / len(change_list)
        greatest_increase = max(change_list)
        greatest_decrease = min(change_list)

    #finding the index of dates of the greatest increase/decrease in profits
    greatest_increase_month_index = change_list.index(greatest_increase) + 1
    greatest_decrease_month_index = change_list.index(greatest_decrease) + 1
    

      

#print out message

print("Financial Analysis")

print("------------------------")

print(f"Total Months: {str(total_months)}")
print(f"Total: {str(total_profit)}")
print(f"Average Change: {str(avg_change)}")
print(f"Greatest Increase in Profits:{month_list[greatest_increase_month_index]} ({greatest_increase})")
print(f"Greatest Increase in Profits: {month_list[greatest_decrease_month_index]} ({greatest_decrease})")
