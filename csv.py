# CSV read data
import csv

#open file
f = open('new.csv')

csv_data = csv.reader(f)

list1=list(csv_data)

print(list1)