#!/usr/bin/python3

"""
Learning lists in Python
"""
import sys
def main():
  print('Learning lists...')  
  fruits = ['apple', 'banana', 'cherry']
  print(fruits)
  print(fruits[1])
  print(len(fruits))

  squares = [1, 4, 9, 16, 25]
  sum = 0
  for num in squares:
    sum += num
  print('Sum of squares:', sum)     

  if 'banana' in fruits:
    print('Banana is in the list of fruits')

  for i in range(100):
    print(i)

  list = ['larry', 'curly', 'moe']
  list.append('shemp')
  list.insert(0, 'james')
  list.extend(['alpha', 'beta'])
  print(list)
  print(list.index('curly'))
  list.remove('moe')
  list.pop(1)
  print(list)
  
if __name__ == '__main__':
  main()
