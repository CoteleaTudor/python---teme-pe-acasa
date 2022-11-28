#    LIFT SIMULATION / realms simulations

#    * conditionals / looping / branching
#    * logic wraping / inside-outside
#    * logical sequences / connections

# + HW1: write the logic for no ROOF and no PAEKING (de desenat linile intrerupte sus/jos)
# + HW2: write the logic for the human inside  the lift
# + HW3: write the logiv that draws lift (de desenat inainte de centru)

DIR_UP              = -1
DIR_stopped         = 0
DIR_down            = 1

from os import system
from time import sleep

building_roof       = True  # FALSE HW1
building_floors     = 9
building_parking    = True  # FALSE HW1

lift_floor          = 3
lift_open           = True
lift_dir            = DIR_stopped 
lift_target_floor   = 3

human_floor         = 6
human_in_lift       = True


"""if lift_floor < lift_target_floor:
    speed = +1
if lift_floor > lift_target_floor:
    speed = -1
if lift_floor == lift_target_floor:
    speed = 0"""

# + HW1: fix the bug with lift bottom at the 1st floor
# + HW2: fix the bug with lift indicator at the 9th floor
# + HW3: add code so when the lift arrives -> human exit

system('cls')
while True:
    
    human_floor     = int(input('Where is the human ? '))
    human_in_lift   = input('Is human inside lift (y/n)? ') == 'y'
    call_lift       = input('Call the lift (y/n)? ')

    if call_lift:
        if not human_in_lift:
            lift_target_floor = human_floor
        else:
            lift_target_floor = int(input('Where to? '))
    else:
        lift_target_floor = lift_floor # daca nu a fost chemat liftul, atunci destinatia este acolo unde te afli
    
    lift_open = False
    
    if lift_floor < lift_target_floor:
        speed = +1
        lift_dir = DIR_UP
    if lift_floor > lift_target_floor:
        speed = -1
        lift_dir = DIR_down
    if lift_floor == lift_target_floor:
        speed = 0
        

    ##### ANIMATION #####
    while True:

        if not DIR_stopped:
            lift_floor += speed
            
            if lift_floor == lift_target_floor:
                if lift_open :
                    lift_open = True
                    lift_dir = DIR_stopped
                
                if human_in_lift:
                    human_in_lift = False
                    human_floor = lift_floor
                else:
                    human_in_lift = True
        
        

        ################### RENDER FRAME ################
        system("cls")

        # pct 3 se mai adauga un if cu conditia la usile deschise
        if building_roof:
            print('---|-----|----')
            print(' R |     |    ')
        #else:                           #punem margina de sus 
             #print('---|-----|----')

        for floor in range(9,0, -1):

            c = '     '
            a = '     '
            t = '     '
            s = ''


            if floor == lift_floor + 1:
                if lift_dir == DIR_down:
                    a = '  v  '
                elif lift_dir == DIR_UP:
                    a = '  ^  '
                elif lift_dir == DIR_stopped and lift_open:
                    a = ' < > '
            elif floor == lift_floor:  
                a = '|   |'
                t = '|---|'
                if human_in_lift:
                    a = '| H |'
            elif floor == lift_floor - 1:
                t = '|---|'
            if floor == human_floor:
                if not human_in_lift:
                    s = ' H'
            if floor == 9 and not building_roof:  # a doua versiune cu podul de sus
                t = '-----'
            print(f'---|{t}|----')
            print(f'{floor:^3}|{a}|{s}')

        if lift_floor == 1:
            t = '|---|'
        else:
            t = '     '

        if building_parking:
            print(f'---|{t}|----')
            print(' P |     |    ')
            print('---|-----|----')

        ################### RENDER FRAME ################

        sleep(.5 )
        if lift_floor == lift_target_floor:
            break

    ##### ANIMATION #####
    sleep(.5 )

