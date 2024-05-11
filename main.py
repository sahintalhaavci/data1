from codes import *
print("You're Welcome :)" , "\nLet's Start Game")
print('Level 1 - Only Remember Numbers','\nLevel 2 - Remember Numbers And Check Hesh','\nLevel 3 - GODMODE')
print('If You Leave Type Exit Or Bye')
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
def st():
    try:
        for i in range(5):
            start()
    except ValueError:
        print('Error')
st()
while True:
    quest = input('Continue (y/n) : ') 
    if quest == 'y':
        st()
    elif quest == 'n':
        print('BYE BYE :D')
        break