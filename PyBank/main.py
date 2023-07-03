import os
import csv

#text file
text_path = "PyBank_output.txt"

total_months = 0
total_revenue = 0
revenue = []
previous_revenue = 0
month_of_change = []
revenue_change = 0
greatest_decrease = ["", 9999999]
greatest_increase = ["", 0]
revenue_change_list = []
revenue_average = 0

#open csv
budgetdata_csv = os.path.join("Resource", "budget_data.csv")
#budgetdata_csv = os.path.join("C:\\Users\\PK\\BootCamp\\Activity\\Assignments\\Assignment 7.5\\Starter_Code\\PyBank\\budget_data.csv")
with open(budgetdata_csv) as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for row in csv_reader:

#count months
        total_months += 1
#count total rev. over the period
        total_revenue = total_revenue + int(row["Profit/Losses"])
#calculate average change in rev between month over time
        revenue_change = float(row["Profit/Losses"])- previous_revenue
        previous_revenue = float(row["Profit/Losses"])
        revenue_change_list = revenue_change_list + [revenue_change]
        month_of_change = [month_of_change] + [row["Date"]]


 #greatest increase in rev (date and amount) over the entire period
        if revenue_change>greatest_increase[1]:
            greatest_increase[1]= revenue_change
            greatest_increase[0] = row['Date']

 #The greatest decrease in rev (date and amount) over the entire period
        if revenue_change<greatest_decrease[1]:
            greatest_decrease[1]= revenue_change
            greatest_decrease[0] = row['Date']
            revenue_average = sum(revenue_change_list)/len(revenue_change_list)

        with open(text_path, 'w') as file:
            file.write("Financial Analysis\n")
            file.write("---------------------\n")
            file.write("Total Months: %d\n" % total_months)
            file.write("Total Revenue: $%d\n" % total_revenue)
            file.write("Average Revenue Change $%d\n" % revenue_average)
            file.write("Greatest Increase in Revenue: %s ($%s)\n" % (greatest_increase[0], greatest_increase[1]))
            file.write("Greatest Decrease in Revenue: %s ($%s)\n" % (greatest_decrease[0], greatest_decrease[1]))

