def game():
    return 49

newScore = game()

with open("hiscore.txt") as file:
    hiscoreStr = file.read()

if hiscoreStr=='':
    with open("hiscore.txt", "w") as file:
        file.write(str(newScore))
        print("Hi-Score Updated!")

elif int(hiscoreStr)<newScore:
    with open("hiscore.txt", "w") as file:
        file.write(str(newScore))
        print("Hi-Score Updated!")
else:
    print("Score was not Updated!")