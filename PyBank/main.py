# Dependencies
import csv
import os

#read csv
csvpath = os.path.join("Resources", "budget_data.csv")

profits = []
month_count = 0


with open(csvpath) as csvfiles:
    csv_reader = csv.reader(csvfiles, delimiter=',')

    #read the header row
    csv_header = next(csvfiles, None)

   # read the actual data row
    next_row = next(csv_reader)

    # assign values/location

    month_count += 1
    value = int(next_row[1])
    total = int(next_row[1])

    greatest_profit = {"Date": next_row[0], "value": 0}
    greatest_loss = {"Date": next_row[0], "value": 0}

    for row in csv_reader:
        month_count += 1
        total = total +int(row[1])

        change = int(row[1])-int(value)

        if len(profits) > 0:
            if change > max(profits):
                greatest_profit["value"] = change
                greatest_profit["Date"] = row[0]
            elif change < min(profits):
                greatest_loss["value"] = change
                greatest_loss["Date"] = row[0]


        profits.append(change)
        value = int(row[1])

       
    average_change = sum(profits)/len(profits)
    greatest_increase_amount = max(profits)
    greatest_decrease_amount = min(profits)

    
   
    print("Financial Analysis")
    print("--------------------------------")
    print("Total Months: " + str(month_count))
    print("Total: $" + str(total))
    print("Average Change: $" + str(round(average_change, 2)))
    print("Greatest Increase in Profits: " + "($" + str(greatest_increase_amount) + ")")
    #print(f"Greatest Increase in Profits: {greatest_increase_amount['Date']}({greatest_increase_amount['value']})")
    print("Greatest Decrease in Profits: " + "($" +str(greatest_decrease_amount) + ")")