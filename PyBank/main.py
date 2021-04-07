#import dependencies
import os
import csv

# Change to the current directory
os.chdir(os.path.dirname(__file__))


# set budget_data_csv to the path for budget_data.csv
budget_data_csv = os.path.join("Resources", "budget_data.csv")

 

#define lists and variables for storing output data
total_months = []
month_count = 0

month_profit_loss = []
date_list =[]
profit_list = []

net_profit = 0
previous_month_profit = 0
current_month_profit = 0
month_profit_change = 0
total_profit_loss = 0

 
#open the csv stored in the budget_data_csv object
with open(budget_data_csv, newline = "\n") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    #skip the header row
    next(csv_file)

    for row in csv_reader:
    
        #append the date list with the date columbn so we can later retrieve the associated dates of our output.
        date_list.append(row[0])

        #append the profit list with the profit column with the profit column so we can perform our profit/loss caluculations.
        profit_list.append(int(row[1]))

        #increment month count by one for each row.
        month_count += 1

        #calculate net profit/loss by adding the current row profit loss to the value stored in net_profit.
        net_profit += int(row[1])

        #set the current month profit to the value in the current rows profit/loss column.
        current_month_profit = int(row[1])

        #if it's the first month, set the previous month profit and current month profit to the same value so it will equal 0. 
        #This is because there is no change for the first row. Add a continue statement to continue looping through the rows.
        if (month_count == 1):
            previous_month_profit = current_month_profit
            continue

        #if it's not the the first month, calculate the month profit/loss change by subtracting the current month profit/loss by the previous month profit/loss.  
        else:

            month_profit_change = current_month_profit - previous_month_profit

            #append the month profit/loss list with the calculated month profit/loss.
            month_profit_loss.append(month_profit_change)

            #keep a running total of the monthly profit/loss so we can calculate the average.
            total_profit_loss = total_profit_loss + month_profit_change

            #set the previous month profit/loss to the current month profit loss so it can be used as the previous month for the next row.
            previous_month_profit = current_month_profit

#get out of the with statement to perform calculations
#calculate the average profit/loss by dividing the total profit/loss by the number of months (minus 1 because there is no change for the first month)
#Sdd the round function to round to 2 decimal places.
average_profit_loss = round(total_profit_loss/(month_count -1), 2)

#calculate the greatest increase and decrease using the min and max functions.
greatest_increase = max(month_profit_loss)
greatest_decrease = min(month_profit_loss)           

#retrieve the greatest increase and decrease dates by passing the greatest increase and decrease values into the index function and returning the associated dates from the date_list.
greatest_increase_date = date_list[month_profit_loss.index(greatest_increase)]
greatest_decrease_date = date_list[month_profit_loss.index(greatest_decrease)]


#print analysis to the terminal.
print("Financial Analysis")
print("---------------------------------------")
print(f"Total Months:  {month_count}")
print(f"Total:  ${net_profit}")
print(f"Average Change:  ${average_profit_loss}")
print(f"Greatest Increase in Profits:  {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Losses:  {greatest_decrease_date} (${greatest_decrease})")

#export results as a text file.
financial_analysis = os.path.join("analysis", "Financial_analysis.txt")
with open(financial_analysis, "w") as output_file:


    output_file.write("Financial Analysis\n")
    output_file.write("---------------------------------------\n")
    output_file.write(f"Total Months:  {month_count}\n")
    output_file.write(f"Total:  ${net_profit}\n")
    output_file.write(f"Average Change:  ${average_profit_loss}\n")
    output_file.write(f"Greatest Increase in Profits:  {greatest_increase_date} (${greatest_increase})\n")
    output_file.write(f"Greatest Decrease in Losses:  {greatest_decrease_date} (${greatest_decrease})\n")