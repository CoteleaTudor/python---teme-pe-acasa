print("\n")

for y in range(1, 11):
    for x in range(1, 11):
        if x == 1:
            print("#", end=" ")
        elif y == 1:
            print("#", end=" ")
        elif x == 10:
            print("#", end=" ")
        elif y == 10:
            print("#", end=" ")
        else:
            print(".", end=" ")
    print()

print("\n")