from os import system
lenght  = 20
roboX   = 5

direction = ""
#GAME LOOP
while direction != "x":
    system("cls")
    #### draw the map########
    print("\n")
    x = 1
    while x <= lenght:
        if x == roboX:
            print("R", end="")
        else:
            print("-", end="")
       
        x += 1
    print("\n")
   
        ###### CONTROLS #########
    direction = input("direct(a/d) >>> ")
    if direction == "a":
        roboX -= 1
    if direction == "d":
        roboX += 1    