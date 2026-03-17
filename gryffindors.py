students = [
    {"name": "Hermione Granger", "house": "Gryffindor"},
    {"name": "Harry Potter", "house": "Gryffindor"},
    {"name": "Draco Malfoy", "house": "Slytherin"},
    {"name": "Ron Weasley", "house": "Gryffindor"}
]

def is_gryffindor(student):
    return student["house"] == "Gryffindor"

# gryffindors = [
#     student["name"] for student in students if is_gryffindor(student)
# ]

gryffindors = filter(is_gryffindor, students)

for gryffindor in sorted(gryffindors, key=lambda student: student["name"]):
    print(gryffindor["name"])

students = ["Hermione Granger", "Harry Potter", "Draco Malfoy", "Ron Weasley"]
gryffindors = []
for student in students:
    gryffindors.append({"name": student, "house": "Gryffindor"})

print(gryffindors)

gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]
print(gryffindors)

for i, student in enumerate(students):
    print(f"{i+1}: {student}")