import csv

with open ("C:\\Users\\shahla\\Desktop\\python\\grades.csv") as f:
    reader = csv.reader(f)
    for i in reader:
        print(type(i))
         