import random



def gameWin():
    if comp == you:
        return None
    if comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    if comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    if comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True

print("Computer's Turn: Snake(s) Water(w) or Gun(g)?")
randNo = random.randint(1,3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo ==3:
    comp = 'g'
print(randNo)

you = input("Your Turn: Snake(s) Water(w) or Gun(g)?")
a = gameWin(comp, you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")    
