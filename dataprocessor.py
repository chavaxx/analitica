import csv

male = 0
female = 0
with open('insurance.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        if(row[1]=="female"):
            female=female +1
        else:
            male=male +1

print(male)
print(female)