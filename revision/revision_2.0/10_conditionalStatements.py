a = int(input("Enter a number between 1 and 100 = "))

if a>1 and a<30:
    print("The number is greater than 1 and less than 30!")
elif a>=30 and a<70:
    print("The number is greater than 30!\n")
elif a>=70 and a<100:
    print("The number is greater than 70!\n")
elif a==100:
    print("The number is itself 100!\n")
else:
    print("The number is neither greater than 30 nor greater than 70!\n")
