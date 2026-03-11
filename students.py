import csv
# with open("names.csv", "r") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         print(f"{name} is in {house}")

students = []

with open("names.csv", "r") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

for student in sorted(students, key=lambda student: student["name"]):
     print(f"{student['name']} is in {student['house']}")

# def get_name(student):
#     return student["name"]

# def get_house(student):
#     return student["house"]

# for student in sorted(students, key=get_house, reverse=False):
#     print(f"{student['name']} is in {student['house']}")

print("Students:")
students = []
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append(row)

for student in sorted(students, key=lambda student: student["name"]):
     print(f"{student['name']} is from {student['home']}")

name = input("What's your name? ")
home = input("Where are you from? ")

with open("students1.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})