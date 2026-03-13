students = [
    {"name": "Hermoine Granger", "house": "Gryffindor"},
    {"name": "Harry Potter", "house": "Gryffindor"},
    {"name": "Ron Weasley", "house": "Gryffindor"},
    {"name": "Draco Malfoy", "house": "Slytherin"},
    {"name": "Padma Patil", "house": "Ravenclaw"},
]

houses = set()
for student in students:
    houses.add(student["house"])

print(houses)   

for each in sorted(houses):
    print(each)