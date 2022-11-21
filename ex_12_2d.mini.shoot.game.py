# * * * * * * * * * * y1
# * * * * * * * * * * 
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * ☠ * * * * *
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *
# * * * < R > * * * y10
from os import system
from time import sleep
from random import randint
# robot coords
rx = 5
coins = 0
# bullet cords
bx = -1
by = -1
# target coords
tx = 5
ty = 3

option = ""
while option != 'x':        # finish game
    ############### DRAW THE MAP #######################(
    system("cls")
    for y in range(1,11):
        for x in range(1,11):   
            if x == rx and y == 10:
                print("R", end=" ")
            elif x == bx and y == by:
                print("☠", end=" ")
            elif x == tx and y == ty:
                print("☆", end=" ")
            else:
                print(".", end=" ")
        print()
    print("score: ", coins)
    sleep(0.05)
    ############### DRAW THE MAP #######################
   
    ############### BULLET #######################
    if by != -1:
        by -= 1
        #HW1:
        #   add a score variable
        #   increment when hitting a target
        if bx == tx and by == ty:
            coins += 10
            ty = randint(1,7)
            tx = randint(1,10)
            #ty = -1
            by = -1
        continue
    ############### BULLET #######################
    
    ############### CONTROL #######################
    option = input(">>>> ")
    if option == 'a':
        rx -= 1
    if option == 'd':
        rx += 1
    if option == ' ':
        bx = rx
        by= 10 - 1
    ############### CONTROL #######################