Start_n = int(input("enter a number for start "))
End_n = int(input("enter a number for end "))

if Start_n > End_n:
    while True:
        print(Start_n)
        if Start_n == End_n:
            break
        Start_n -= 1

elif Start_n <= End_n and End_n / Start_n ==2:
    while True:
        print(Start_n)
        if Start_n == End_n:
            break
        Start_n += 1

else:
 print("EROR: the second number must be 2 times higer than the first, please reply the cod")