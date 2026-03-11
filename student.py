# def main():
#     name = get_name()
#     house = get_house()
#     print(f"{name} from {house}")

# def get_name():
#     name = input("Name:  ").strip()
#     return name

# def get_house():
#     house = input("House: ").strip()
#     return house

class Student:
    def __init__(self, name, house):

        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"
    
def get_student():
    name = input("Name:  ")
    house = input("House: ")

    student = Student(name, house)
    return student

def main():
    student = get_student()
    # print(f"{student.name} from {student.house}")
    print(student)

if __name__ == "__main__":
    main()
