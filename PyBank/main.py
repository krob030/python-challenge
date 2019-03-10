import os
import csv
csvpath= os.path.join("C:/Users/karsa_000/Desktop/Boot Camp/module 3/HWK/budget_data.csv")
with open(csvpath, newline='') as csvfile:
    csvreader= csv.reader(csvfile, delimiter=',')   
    csv_header = next(csvreader)
    #print(f"Header: {csv_header}")
    Total_months = 0
    for row in csvreader:
      Total_months += 1
    print (Total_months)