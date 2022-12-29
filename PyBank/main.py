# import modules
import os
import csv

# path to csv file
csvpath = os.path.join("Resources","budget_data.csv")

# create lists
profit = []
month = []
change = []

# read csv data 
with open (csvpath, encoding = "utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)
    

# loop through to collect data on number of months and total profit
    for row in csvreader:

        month.append(row[0])
        profit.append(int(row[1]))
        
    #print(f"Months: {len(month)}")
    #print(f"Total profit/losses: ${sum(profit):,}")


# find the monthly profit gain/loss and the average gain/loss
for x in range(1, len(month)):
    
    gain =  (profit[x]) - (profit[x-1])
    change.append(gain)
    
avg_profit = round(sum(change)/len(change),2)
#print(avg_profit)


# find the month & value of maximum profit gain
profit_max = max(change)
profit_max_index = change.index(profit_max)

#print(profit_max)
#print(month[profit_max_index+1])


# find the month & value of maximum profit loss
profit_min = min(change)
profit_min_index = change.index(profit_min)

#print(profit_min)
#print(month[profit_min_index + 1])


# print results to terminal
print()
print("Financial Analysis")
print("----------------------------------------------------")
print((f"Totals Months: {len(month)}"))
print(f"Total profit/losses: ${sum(profit):,}")
print(f"Average change: ${avg_profit:,}")
print(f"Greatest Increase in Profits: {month[profit_max_index+1]} $({profit_max:,})")
print(f"Greatest Decrease in Profits: {month[profit_min_index+1]} $({profit_min:,})")
print("----------------------------------------------------")


# output results to a text file in analysis folder
text_file = []
output_path = os.path.join("analysis","financial_analysis.txt")


text_file.append("Financial Analysis")
text_file.append("----------------------------------------------------")
text_file.append(f"Totals Months: {len(month)}")
text_file.append(f"Total profit/losses: ${sum(profit):,}")
text_file.append(f"Average change: ${avg_profit:,}")
text_file.append(f"Greatest Increase in Profits: {month[profit_max_index+1]} $({profit_max:,})")
text_file.append(f"Greatest Decrease in Profits: {month[profit_min_index+1]} $({profit_min:,})")
text_file.append("----------------------------------------------------")

with open(output_path, 'w') as text:
    for line in text_file:
        text.write(line)
        text.write('\n')