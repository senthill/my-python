#!/usr/bin/env python3
""" Python sorting """

from operator import itemgetter

def main():
    numbers = [5, 2, 9, 1, 5, 6]
    print("Original list:", numbers)
    numbers.sort()
    print("Sorted list:", numbers)

    strs = ['aa', 'BB', 'cc', 'DD', 'ee']
    print(sorted(strs))
    print(sorted(strs, reverse=True))
    print(sorted(strs, key=str.lower))
    print(sorted(strs, key=str.lower, reverse=True))

    grades = [('Freddy', 'Frank', 3), ('Anil','Frank', 100), ('Anil', 'Wang', 50)]
    print(sorted(grades, key=itemgetter(1)))
    print(sorted(grades, key=itemgetter(2), reverse=True))
    print(sorted(grades, key=itemgetter(0)))


if __name__ == '__main__':
    main()