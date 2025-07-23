user_input = int(input("Enter the size of the pattern:"))
x = 0

while x < user_input:
    y = 0
    while y < user_input:
        print("*", end="")
        y += 1
    x += 1
    print()