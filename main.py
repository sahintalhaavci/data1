from codes import *
print("You're Welcome :)" , "\nLet's Start Game")
print('Level 1 - Only Remember Numbers','\nLevel 2 - Remember Numbers And Check Hesh','\nLevel 3 - GODMODE')
try:
    choose = int(input('Please Select Level : '))
except ValueError:
    print('Type 1 , 2 or 3!!')

def start():
    if choose == 1:
        saver()
    elif choose == 2:
        saver()
        history()
    elif choose == 3:
        while True:
            print("You're NUB")
try:
    while True:
        start()
except:
    print()