#import and open csv file
from operator import indexOf
import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

#Set variables
months = []
sales = []
salechange = 0
monthlysalechange = []

with open(csvpath) as csvfile:  

    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    #print(header)
    
    for row in csvreader:
         months.append(row[0])
         sales.append(int(row[1]))

# print(months)
# print(sales)


#Find total months included in financial records
totalmonths = len(months)
#print(totalmonths)

#Find total "Profit/Losses"
totalsales = sum(sales)
#print(totalsales)
for i in range(len(sales)-1):
    salechange = sales[i+1] - sales[i]
    #print(salechange)
    monthlysalechange.append(salechange)
    #print(monthlysalechange)

averagechange = round(sum(monthlysalechange)/(len(sales)-1), 2)
#print(averagechange)

maxincrease = max(monthlysalechange)
maxdecrease = min(monthlysalechange)
# print(maxdecrease)
# print(maxincrease)

change =monthlysalechange.index(maxincrease)
change2 =monthlysalechange.index(maxdecrease)

increasedate = months[change+1] 
decreasedate = months[change2+1]
# print(increasedate)
# print(decreasedate)

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {totalmonths}")
print(f"Total: ${totalsales}")
print(f"Average Change: ${averagechange}")
print(f"Greatest Increase in Profits: {increasedate} (${maxincrease})")
print(f"Greatest Decrease in Profits: {decreasedate} (${maxdecrease})")

#export to text file
outpath = os.path.join('analysis', 'pybank_output.txt')
with open(outpath, "w") as text:
        text.write('Financial Analysis\n')
        text.write('----------------------------\n')
        text.write(f"Total Months: {totalmonths}\n")
        text.write(f"Total: ${totalsales}\n")
        text.write(f"Average Change: ${averagechange}\n")
        text.write(f"Greatest Increase in Profits: {increasedate} (${maxincrease})\n")
        text.write(f"Greatest Decrease in Profits: {decreasedate} (${maxdecrease})\n")

    
