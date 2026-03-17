# MEOWS = 3

# for i in range(MEOWS):
#     print("meow")

# class Cat:
#     MEOWS = 3

#     def meow(self):
#         for i in range(self.MEOWS):
#             print("meow")
    
# cat = Cat()
# cat.meow()

def meow(n: int) -> None:
    """ Prints n meows
        :param n: number of meows
        :return: None
    """
    for i in range(n):
        print("meow")

number = int(input("Number of meows: "))
# number = input("Number of meows: ")
# meow(number)

meows: str = meow(number)
print(meows)