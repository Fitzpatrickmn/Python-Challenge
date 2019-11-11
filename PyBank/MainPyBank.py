# 1 - Total Months in Data Set 
# net total amount of "Profit/Losses" over the entire period
# average of the changes in "Profit/Losses" over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period
# In addition, your final script should both print the analysis to the terminal and export a text file with the results.


import os
os.chdir("/Users/michellefitzpatrick/Python-Challenge")
import csv
csvpath = os.path.join("PyBank", "Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv")

totalmonths = 0
totalrevenue = 0
revenuechanges = []
greatestincrease = 0
greatestdecrease = 0
greatestmonth = ""
lowestmonth = ""

with open(csvpath, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csv_reader)

    # Read through each row of data after the header
    matrix =[]
    for row in csv_reader:
        matrix.append(row)
    totalmonths = len(matrix)
    PL_value_list = []
    month_val_list =[]

    for i in range(len(matrix)):
        PL_value_list.append(int(matrix[i][1]))
        month_val_list.append(matrix[i][0])
    totalrevenue = sum(PL_value_list)

    avg_val_list = []
    for i in range(len(PL_value_list)):
        if i == 0:
            temp = PL_value_list[i]
        else:
            avg_val_list.append(PL_value_list[i]-temp)
            temp = PL_value_list[i]

    avg_rev_change = float(sum(avg_val_list))/float(len(avg_val_list))
    avg_rev_change = round(avg_rev_change,2)

    greatestincrease = max(avg_val_list)
    max_val_index = avg_val_list.index(greatestincrease) + 1
    greatestmonth = month_val_list[max_val_index]

    greatestdecrease = min(avg_val_list)
    min_val_index = avg_val_list.index(greatestdecrease) + 1
    month = month_val_list[min_val_index]
    lowestmonth = month_val_list[min_val_index]

print(f"Financial Analysis")
print(f"----------------------")
print(f"Total: " "$"+str(totalrevenue))
print(f"Total Months: " +str(totalmonths))
print(f"Average Change: ","$"+str(avg_rev_change))
print(f"Greatest Increase in Profits: ",(greatestmonth),"$"+str(greatestincrease))
print(f"Greatest Decrease in Profits: ",(lowestmonth),"$"+str(greatestdecrease))

PyBank_Output = os.path.join('PyBank','budgetdataoutput1.txt')
with open (PyBank_Output, 'w') as txtfile:
    txtfile.write(f"Financial Analysis \n")
    txtfile.write(f"---------------------- \n")
    txtfile.write(f"Total Months: {totalmonths}\n")
    txtfile.write(f"Total: ${totalrevenue}\n")
    txtfile.write(f"Average Change: ${avg_rev_change} \n")
    txtfile.write(f"Greatest Increase in Profits: {greatestmonth} (${(greatestincrease)}) \n")
    txtfile.write(f"Greatest Decrease in Profits: {lowestmonth} (${greatestdecrease}) \n")
        



