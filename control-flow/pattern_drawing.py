user_input = int(input("Enter the size of the pattern:"))
x = 0

while x < user_input:
    line = "*" * user_input
    print(f"{line}", end = " ")
    x += 1