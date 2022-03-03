#Teena Tom - 42
import csv
with open('people.csv')as csvfile:
 data = csv.DictReader(csvfile)
 print("Employee name")
 print("---------------------------------")
 for row in data:
   print(row['Name'],row['Age'])