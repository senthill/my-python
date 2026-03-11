#!/usr/bin/python3

import sys

def main():
  print('Learning strings...')
  str1 = 'vanakkam'
  print(str1[2])
  print(len(str1))
  print(str1 + ' nanba')
  
  pi = 22/7
  print('The value of pi is -> ' + str(pi))

  raw = r'this is a raw string \n \t \\'
  print(raw)

  print()

  multi = """ This is a multi-line string.
It can span multiple lines.
    It preserves whitespace and line breaks. """
  print(multi)

  str2 = 'dilmaha '
  print(str2.lower())
  print(str2.upper())
  print(str2.capitalize())
  print(str2.replace('ma', 'tha'))
  print(str2.find('ma'))
  print('ma' in str2)
  print(str2.strip())
  print(str2.split('i')) 
  print(str2.join(['a', 'b', 'c', 'd']))
  print(str2.isalpha())
  print(str2.isdigit())
  print(str2.startswith('di'))
  print(str2.endswith('ha '))
  print(str2.find('x'))

  str3 = 'Vanakkam'
  print(str3[1:5])
  print(str3[:4])
  print(str3[:])
  print(str3[1:100])
  print(str3[-4:-1])
  print(str3[-3:])
  print(str3[::-1])  # Reverse the string

  print(f'The value of pi is approximately {pi:.3f}')

  car = {'tires:4', 'doors:4', 'color:red'}
  print(f'The car has {len(car)} features: {car}')

  print()
  print('Formatted Address Book:')
  address_book = [{'name':'N.X.', 'addr':'15 Jones St', 'bonus': 70},
      {'name':'J.P.', 'addr':'1005 5th St', 'bonus': 400},
      {'name':'A.A.', 'addr':'200001 Bdwy', 'bonus': 5},]

  for person in address_book:
    print(f'{person["name"]:8} || {person["addr"]:20} || {person["bonus"]:>5}')

  # % operator
  text = "%d little pigs come out, or I'll %s, and I'll %s, and I'll blow your %s down." % (3, 'huff', 'puff', 'house')
  print(text)

  text = (
    "%d little pigs come out, "
  "or I'll %s, and I'll %s, "
  "and I'll blow your %s down." % (3, 'huff', 'puff', 'house')
  )
  print(text)

  byte_str = b'This is a byte string'
  print(byte_str)

  ustring = 'A unicode \u018e string \xf1'
  b = ustring.encode('utf-8')
  b
  b'A unicode \xc6\x8e string \xc3\xb1'  ## bytes of utf-8 encoding. Note the b-prefix.
  t = b.decode('utf-8')                ## Convert bytes back to a unicode string
  t == ustring                         ## It's the same as the original, yay!
  print()
  print(ustring)
  print(t)

  time_hour = sys.argv[1] if len(sys.argv) > 1 else 10
  time_hour = int(time_hour)
  if time_hour >= 0 and time_hour < 12:
    part_of_day = 'morning'
  elif time_hour >= 12 and time_hour < 17:
    part_of_day = 'afternoon'
  else:
    part_of_day = 'evening'
  print(f'Good {part_of_day}!')


# Standard boilerplate to call the main function.
if __name__ == '__main__':
  main()
