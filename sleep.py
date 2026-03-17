def main():
    n = int(input("Enter a number: "))
    for s in sheep(n):
        print(s)

# def sheep(n):
#     flock = []
#     for i in range(n):
#         flock.append("🐏" * i)
#     return flock

def sheep(n):
    for i in range(n):
        yield "🐏" * i

if __name__ == "__main__":
    main()