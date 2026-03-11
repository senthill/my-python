#!/usr/bin/env python3
""" Python dictionaries """
def main():
    student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
    print("Original dictionary:", student)

    # Accessing values
    print("Name:", student['name'])
    print("Age:", student.get('age'))

    # Adding a new key-value pair
    student['grade'] = 'A'
    print("After adding grade:", student)

    # Updating an existing value
    student['age'] = 26
    print("After updating age:", student)

    # Removing a key-value pair
    del student['courses']
    print("After removing courses:", student)

    # Iterating through keys and values
    for key, value in student.items():
        print(f"{key}: {value}")

    # Dictionary comprehension
    squares = {x: x*x for x in range(6)}
    print("Dictionary of squares:", squares)

    dict = {}
    dict['a'] = 'alpha'
    dict['b'] = 'beta'
    dict['g'] = 'gamma'
    print("Custom dictionary:", dict)
    print("Keys:", dict.keys())
    print("Values:", dict.values())
    print("Items:", dict.items())
    print("Get 'b':", dict.get('b'))

    for key in dict:
        print(f"{key}: {dict[key]}")

    for key in dict.keys():
        print(f"Key: {key}")

    for key in sorted(dict.keys()):
        print(f"Sorted Key: {key}")

    for k, v in dict.items():
        print(f"Key: {k}, Value: {v}")

    del dict['b']
    print("After deleting 'b':", dict)

    del dict
    print("After deleting dict:", dict)
if __name__ == '__main__':
    main() 