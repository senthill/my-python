#!/usr/bin/python3

""" My first python program to check if the python is working 
and try a simple function.
"""

import sys

# The main function
def main():
  # Check the number of arguments
  if len(sys.argv) >= 2:
    name = sys.argv[1]
  else:
    name = 'Nanba'
  print('Hello', name) 
  
  print(repeat('Hello', False))
  print(repeat('Hello', True))
  

def repeat(s, exclaims):
  """Returns a string that is repeated twice """
  return (s + '! ') * 4
  
# This is a standard boilerplate that calls the main function
if __name__ == '__main__':
  main()