import os
import csv
csvpath= os.path.join("C:/Users/karsa_000/Desktop/Boot Camp/module 3/HWK/budget_data.csv")
with open(csvpath, newline='') as csvfile:
    csvreader= csv.reader(csvfile, delimiter=',')   
    # removing header
    csv_header = next(csvreader)
    Total_months = 0
    for line in csvreader:
      Total_months += 1
    #print (Total_months)
with open(csvpath, newline='') as csvfile:
    csvreader= csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    column_sum = 0
    for line in csvreader:
        column_sum += int(line[1])
    #print(column_sum)
with open(csvpath, newline='') as csvfile:
    csvreader= csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    # extract first line
    first_line = next(csvreader)
    # init previous value
    prev = 0
    # init current value
    current = int(first_line[1])
    # list of differences
    diff_list = []
    # calculate difference
    difference = current - prev
    diff_list.append(difference)
    for line in csvreader:
        prev = current
        current = int(line[1])
        difference = current - prev
        diff_list.append(difference)
    GI= max(diff_list)
    GD= min(diff_list)
    #print(max(diff_list))
    #print(min(diff_list))
print("Financial Analysis")
print("----------------------------")
print("Total Months: "+ str(Total_months))
print("Total: $"+ str(column_sum))
print("Average  Change: $")
print("Greatest Increase in Profits: "+ "($" + str(GI)+ ")")
print("Greatest Decrease in Profits: "+ "($" + str(GD)+ ")")
text_file = open("Output.txt", "w")
text_file.write("Financial Analysis"+ '\n')
text_file.write("----------------------------"+ '\n')
text_file.write("Total Months: "+ str(Total_months)+ '\n')
text_file.write("Total: $"+ str(column_sum)+ '\n')
text_file.write("Average  Change: $"+ '\n')
text_file.write("Greatest Increase in Profits: "+ "($" + str(GI)+ ")"+ '\n')
text_file.write("Greatest Decrease in Profits: "+ "($" + str(GD)+ ")"+ '\n')
text_file.close()