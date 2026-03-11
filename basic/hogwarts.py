#!/usr/bin/env python3

students = ["Harry", "Hermione", "Ron", "Draco"]
houses = ["Ravenclaw",  "Gryffindor", "Slytherin"]

for student in students:
    print(student)

students = {
    "Harry": "Gryffindor",
    "Hermione": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}

print (students["Harry"])
print (students["Draco"])

for student in students:
    print(student, students[student], sep=", ")

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")