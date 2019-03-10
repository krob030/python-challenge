import os
import csv
csvpath= os.path.join("C:/Users/karsa_000/Desktop/Boot Camp/module 3/HWK/election_data.csv")
with open(csvpath, newline='') as csvfile:
    csvreader= csv.reader(csvfile, delimiter=',')   
    csv_header = next(csvreader)