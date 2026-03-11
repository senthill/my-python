import re


name = input("Enter your name: ").strip()

# if "," in name:
#     last, first = name.split(",")
#     name = f"{first} {last} "

# print(f"Hello, {name}!")

# matches = re.search(r"^(.+), *(.+)$", name)
if matches:= re.search(r"^(.+), *(.+)$", name):
    last, first = matches.groups()
print(f"Hello, {first} {last}!")