# import sys
# if (len(sys.argv) == 1):
#     print("meow")
# elif len(sys.argv) == 3 and sys.argv[1] == "-n":
#     try:
#         n = int(sys.argv[2])
#     except ValueError:
#         print("usage: meows1.py")
#     else:
#         for _ in range(n):
#             print("meow")
# else:
#     print("usage: meows1.py")

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--number", dest="n", default=1, help="number of meows", type=int)
args = parser.parse_args()

for _ in range(args.n):
    print("meow")