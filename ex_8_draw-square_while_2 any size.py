from os import system

system ("cls")
size_a  = int(input('size a: '))
size_b  = int(input('size b: '))
lenght = size_a * size_b
n = 1

print()

while n <= lenght:
    print("* ", end="")

    if n % size_b == 0:
        print()
        
    n += 1

print()
