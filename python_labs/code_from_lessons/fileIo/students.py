import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name","home"])
    writer.writerow({"name": name, "home": home})


# using csv.writer
# name = input("What's your name? ")
# home = input("Where's your home? ")
# house = input("Which house do you belong to? ")

# with open("students.csv", "a") as file:
#     writer = csv.writer(file)
#     writer.writerow([name,home,house])


# Not using csv module
# students = []

# with open("students.csv") as file:
#     for line in file:
#         name,house = line.rstrip().split(",",1)
#         student = {"name": name, "house": house}
#         students.append(student)

# for student in sorted(students,key=lambda student: student['name']):
#     print(f"{student['name']} is in {student['house'].replace("\"","")}")

# Using csv.reader
# students = []

# with open("students.csv") as file:
#     reader = csv.reader(file)
#     for name,home in reader:
#         students.append({"name": name, "home": home})

# for student in sorted(students,key=lambda student: student['name']):
#     print(f"{student['name']} is from {student['home'].replace("\"","")}")

# Using csv.DictReader
# students = []

# with open("students.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append(row)

# for student in sorted(students,key=lambda student: student['name']):
#     print(f"{student['name']} is from {student['home']} and belongs to house {student['house']}")
# Print the DictReader's organized output to see how key/values are associated based on the headings
# print(students)