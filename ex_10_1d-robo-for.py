from os import system

rooboX  = 5
roboHP  = 100
roboBT  = 100
bombX   = 7
bombY   = 3
heart1  = 2
heart2  = 6
coins   = 100
star1   = 1
star2   = 9

LENGHT  = 10
option  = " "

# game loop
# 1. draw the map
# 2. read the input
# 3. decide
while True:
########## DRAW MAP ################
    system("cls")
    print("\n")

    for x in range(1, LENGHT + 1):        # 1....10
        if x == rooboX:
            print("♔", end=" ")
        elif x == bombX:
            print("☠", end=" ")
        elif x == bombY:
            print("☠", end=" ")
        elif x == heart1:
            print("♥", end=" ")
        elif x == heart2:
            print("♥", end=" ")
        elif x == star1:
            print("☆", end=" ") 
        elif x == star2:
            print("☆", end=" ")       
        else:
            print("●", end=" ")
    print("\nHP:    ", roboHP, "♥")
    print("BT:    ", roboBT, "%" )
    print("Score: ", coins, "%" )
    print("\n")
########## DRAW MAP ################

    ########## 2. READ INPUNT ################

    option = input(">>>> ")

    ########## 2. READ INPUNT ################

    ########## 3. DECIDE ################
    if option == "a" and rooboX > 1:   # move left
        rooboX -= 1
        roboBT -= 1
        coins += 10
    if option == "d" and rooboX < 10:   # move right
        rooboX += 1
        roboBT -= 1
        coins += 10

    # check if bomb
    if rooboX == bombX and roboHP > 0:
        roboHP -= 10
        coins  -= 25
        bombX = "●"
    if rooboX == bombY and roboHP > 0:
        roboHP -= 10
        coins  -= 25
        bombY = "●"
    
    # check if heart
    if rooboX == heart1:
        roboHP += 10
        coins  += 10
        heart1 = "●"
    if rooboX == heart2:
        roboHP += 10
        coins  += 10
        heart2 = "●"
    
     # check if star
    if rooboX == star1:
        coins += 25
        star1 = "●"
    if rooboX == star2:
        coins += 25
        star2 = "●"

    if option == "x":
        system("cls")
        print("thank you for game! :) ")
        break      
    ########## 3. DECIDE ################

# + HW1: frontier check RIGHT and LEFT
# + HW2: second bomb 
# HW3: place some hearts --> HP+   
# HW4*: place some coins --> score+ 
# HW5*: add variables --> state of boms, coins ... 
# HW6*: if all line = . -->  game won