import random
from typing import no_type_check


def game(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True


print("computer's turn:snake(s) water(w) or gun(g)?")
randno = random.randint(1, 3)
if randno == 1:
    comp = 's'
elif randno == 2:
    comp = 'w'
elif randno == 3:
    comp = 'g'
you = input("your turn:snake(s) water(w) or gun(g)?\n")

if you == 's':
    print(f"your chosen key is {you}")
elif you == 'w':
    print(f"your chosen key is {you}")
elif you == 'g':
    print(f"your chosen key is {you}")
else:
    print('''                                                      your chosen key is not valid
                                            choose betweet the prefix of snake,water or gun's ''')

a = game(comp, you)

print(f"computer chose {comp}")

if comp == you:
    print("its a tie because you both chose the same keyword")
elif comp == 'w' and you == 'g':
    print(f"comp wins bcs it choses {comp} and you chose {you}")
elif comp == 'w' and you == 's':
    print(f"comp loses bcs it choses {comp} and you chose {you}")
elif comp == 'g' and you == 's':
    print(f"comp wins bcs it choses {comp} and you chose {you}")
else:
    print("NOW IT IS FUN ^.^ KEEP PLAYING")







