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
    def __init__(self, name, house, patronus=None):

        if not name:
            raise ValueError("Missing name")
        # if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
        #     raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house} is a {self.patronus}"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name
    
    # Getter 
    @property
    def house(self):
        return self._house
    
    # Setter
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house
    
    def charm(self):
        match self.patronus:

            case "Stag":
                return "🦌"
            case "Otter":
                return "🦦"
            case "Jack Russell Terrier":
                return "🐶"
            case _:
                return "🪄"

    
def get_student():
    name = input("Name:  ")
    house = input("House: ")
    patronus = input("Patronus: ")

    student = Student(name, house, patronus)
    return student

def main():
    student = get_student()
    # print(f"{student.name} from {student.house}")
    # print(student)
    # print("Expecto Patronum! ", end="")
    # print(student.charm())
    # student.house = "Number 4 Privet Drive"
    print(student)

if __name__ == "__main__":
    main()
