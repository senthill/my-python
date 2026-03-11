def main():
    print_square(5)

def print_square(size):
    # For each row in the square
    for i in range(size):
        # For each column in the square
        print_row(size)
        print()

def print_row(size):
    print("#" * size, end="")

main()