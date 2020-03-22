# Dependencies
import csv
import os

#read csv
csvpath = os.path.join("Resources", "budget_data.csv")

#initialize
profits = []
months = 0


with open(csvpath) as csvfiles:
    csv_reader = csv.reader(csvfiles, delimiter=',')

    #read the header row
    csv_header = next(csvfiles, None)

   # read the actual data row
    next_row = next(csv_reader)

    # assign values/location

    months += 1
    value = int(next_row[1])
    total = int(next_row[1])

    profit = {"date": next_row[0], 
                       "value": 0}
    loss =   {"date": next_row[0], 
                     "value": 0}

    for row in csv_reader:
        months += 1
        total = total +int(row[1])

        change = int(row[1])-int(value)

        if len(profits) > 0:
            if change > max(profits):
                profit["date"] = row[0]
                profit["value"] = change
                
            elif change < min(profits):
                loss["date"] = row[0]
                loss["value"] = change
                


        profits.append(change)
        value = int(row[1])

       
    average_change = sum(profits)/len(profits)
    

    
   
    print("Financial Analysis")
    print("--------------------------------")
    print("Total Months: " + str(months))
    print("Total: $" + str(total))
    print("Average Change: $" + str(round(average_change, 2)))
    print(f'Greatest Increase in Profits: {profit["date"]} (${profit["value"]})')
    print(f'Greatest Decrease in Profits: {loss["date"]} (${loss["value"]})')
   