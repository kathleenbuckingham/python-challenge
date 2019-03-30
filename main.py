#Import csv
import os
import csv

#Create file variable
# pyBankCSV = os.path.join(".","pyBank.csv")

os.chdir("PyBank")

with open("pyBank.CSV", newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

#Define the function and have it accept pyBankData as the sole function
    
    Total_months = 0.00
    Net_total = 0.00
    average = 0.00
    Greatest_increase = ["",0.00]
    Greatest_decrease = ["",0.00]

    for row in csvreader:
        Total_months += 1
        Net_total += float(row[1])
        current_change = float(row[1])
        
        if current_change > Greatest_increase[1]:
            Greatest_increase[0] = row[0]
            Greatest_increase[1] = float(row[1])
        else:
            current_change < Greatest_decrease[1]
            Greatest_decrease[0] = row[0]
            Greatest_decrease[1] = float(row[1])

print(f"Total Months: {Total_months}")
print(f"Net Total: {Net_total}")
print(f"Average: {Net_total/Total_months}")
print(f"Greatest Profit: ${Greatest_increase[1]} occurred in {Greatest_increase[0]}")
print(f"Greatest Decrease: ${Greatest_decrease[1]} occurred in {Greatest_decrease[0]}")
    
  

     