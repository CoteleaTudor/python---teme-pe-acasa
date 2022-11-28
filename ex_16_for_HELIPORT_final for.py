SCALE  = 10

hX = 4
hY = 4

map = "" 
for y in range(SCALE):
    map += str(y) + ". "
    for x in range(SCALE,):
        # print harta cu zgomot
        if x == 0 or x == SCALE - 1 or y == 0 or y == SCALE - 1:
            map += "# "
            # stinga si dreapta 
        elif x == hX - 1 and y == hY:
            map += "~ "
        elif x == hX - 2 and y == hY:
            map += "~ "
        elif x == hX + 1 and y == hY:
            map += "~ "
        elif x == hX + 2 and y == hY:
            map += "~ "
        # sus si jos
        elif x == hX and y == hY - 1:
            map += "~ "
        elif x == hX and y == hY + 1:
            map += "~ "
        elif x == hX and y == hY - 2:
            map += "~ "
        elif x == hX and y == hY + 2:
            map += "~ "
        
        # diagonale
        elif x == hX - 1 and y == hY - 1:
            map += "~ "
        elif x == hX + 1 and y == hY + 1:
            map += "~ "
        elif x == hX - 1 and y == hY + 1:
            map += "~ "
        elif x == hX + 1 and y == hY - 1:
            map += "~ "
       
        elif x == hX + 2 and y == hY - 1:
            map += "~ "
        elif x == hX + 1 and y == hY - 2:
            map += "~ "
        elif x == hX - 1 and y == hY + 2:
            map += "~ "
        elif x == hX - 2 and y == hY + 1:
            map += "~ "
       
        elif x == hX + 2 and y == hY + 1:
            map += "~ "
        elif x == hX + 1 and y == hY + 2:
            map += "~ "
        elif x == hX - 1 and y == hY - 2:
            map += "~ "
        elif x == hX - 2 and y == hY - 1:
            map += "~ "
        elif x == hX and y == hY:
            map += "H "
        else:
            map += "  "

    map += "\n"                

print(map)


""" Trebuie sa afiseze in felul urmator

 1. # # # # # # # # # # 
 2. #     ~ ~ ~       # 
 3. #   ~ ~ ~ ~ ~     # 
 4. #   ~ ~ H ~ ~     # 
 5. #   ~ ~ ~ ~ ~     # 
 6. #     ~ ~ ~       # 
 7. #                 # 
 8. #                 # 
 9. #                 # 
10. # # # # # # # # # # 
"""