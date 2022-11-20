# * * * * * * * * * * y1
# * * * * * * * * * * 
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * * y10
rx  = 5
ry  = 5

print()

for y in range (1, 11):
    for x in range (1, 11):
        if x == rx and y == ry:
            print("R", end=" ")
        # diagonals
        #elif x == y == ry - 1:
           #print("a", end=" ")
       # elif x == y == ry + 1:
           # print("b", end=" ")    
        elif x == y == rx + 1:
            print("c", end=" ")            
        # up and down
        elif x == rx and y == ry - 1:
            print("+", end=" ")
        elif x == rx and y == ry + 1:
            print("+", end=" ")
        # left and right    
        elif x == rx - 1 and y == ry:
            print("+", end=" ")
        elif x == rx + 1 and y == ry:
            print("+", end=" ")                      
        
        else:
            print(".", end=" ")    
    print()

print()

#HW1*: Diagonal directions