# FACT: list of friends>


# empty list

friend = []

while len(friend) < 100:
    name = input("add friend name:  ")
    if name == "": # cand apasam enter
        break
    # HW1: check if the name is in the list
        # opertor in
    if name not in friend:
        friend.append(name)
    #else:    
       # break

print("you have", len(friend), "friends")
for i in range(len(friend)):
    print("   ",i,">>", friend[i])