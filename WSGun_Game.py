
import random
from typing import no_type_check
print("computer's turn:snake(s) water(w) or gun(g)?")
randno=random.randint(1,3)
if randno==1:
    comp='s'
elif randno==2:
    comp='w'
elif randno==3:
    comp='g'
you=input("your turn:snake(s) water(w) or gun(g)?\n")
def game(comp,you):
    if comp==you:
        print("its a tie")
        return None
    elif comp=='s':
        if you=='w':
            print("you lost!")
            return False
        elif you=='g':
            print("you won")
            return True
    elif comp=='w':
        if you=='g':
            print("you lost")
            return False
        elif you=='s':
            print("you won")
            return True
    elif comp=='g':
        if you=='s':
            print("you lost")
            return False
        elif you=='w':
            print("you won")
            return True
print(f"computer chose {comp}")


if you=='s':
    print(f"your chosen key is {you}")
elif you=='w':
    print(f"your chosen key is {you}")
elif you=='g':
    print(f"your chosen key is {you}")
else:
    print('''                                                      your chosen key is not valid
                                            choose betweet the prefix of snake,water or gun's ''' )

a=game(comp,you)

