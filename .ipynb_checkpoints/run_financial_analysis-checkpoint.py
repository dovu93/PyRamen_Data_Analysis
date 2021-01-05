import csv

months = []
profit = []
monthly_change = []

count = 0
end_profit = 0
random = 0
greatest_increase = 0
greatest_decrease = 0
starting_profit = 0

with open("Data/budget_data.csv", "r") as csv_file:
    df = csv.reader(csv_file)
    next(df)
    
    for row in df:
        
        count = count + 1
        
        months.append(row[0])
        
        profit.append(int(row[1]))
        
        end_profit = end_profit + int(row[1])
        
        avg_gains = end_profit / count
        
        monthly_profit = int(row[1])
        
        if starting_profit == 0:
            monthly_change.append(0)
            starting_profit = monthly_profit       
        else:
            ending_profit = monthly_profit - starting_profit
            monthly_change.append(ending_profit)
            starting_profit = monthly_profit
        
        
        
greatest_increase = max(monthly_change)
greatest_decrease = min(monthly_change)
        
greatest_month = months[monthly_change.index(greatest_increase)]
lowest_month = months[monthly_change.index(greatest_decrease)] 

for ro in monthly_change:
    random += ro
    
avg_change = random/count

print("Financial Analysis PyRamen")
print("----------------------------------------")
print("Total Months: "+ str(count))
print("Total Profits: $ " + str(end_profit))
print("Average Monthly Change: $", "{:.2f}".format(avg_change))
print("Greatest Increase in Profits: "+str(greatest_month) + " $ " + str(greatest_increase))
print("Greatest Decrease in Profits: "+str(lowest_month) + " $ " + str(greatest_decrease))
print("----------------------------------------")


with open('Financial_Analysis_PyRamen.txt', 'w') as text:
    text.write("Financial Analysis PyBank" + "\n")
    text.write("-----------------------------------------------------------" + "\n")
    text.write("    Total Months: " + str(count) + "\n")
    text.write("    Total Profits: $" + str(end_profit) + "\n")
    text.write("    Average Monthly Change: $")
    text.write("{:.2f}".format(avg_change) + "\n")
    text.write("    Greatest Increase in Profits: "+str(greatest_month) + " $ " + str(greatest_increase) + "\n")
    text.write("    Greatest Decrease in Profits: "+str(lowest_month) + " $ " + str(greatest_decrease) + "\n")
    text.write("------------------------------------------------------------" + "\n")