import random
class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        return random.choice(cls.houses)

house = Hat.sort("Harry")
print(f"Harry is in {house}")