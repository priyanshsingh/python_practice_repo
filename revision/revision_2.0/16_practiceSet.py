a = int(input("Enter a number 1 = "))
b = int(input("Enter a number 2 = "))
c = int(input("Enter a number 3 = "))

def greatest_of_three(a, b, c):
    if a>b and a>c:
        print("\n" + str(a) + " is greatest!\n")
    elif b>c and b>a:
        print("\n" + str(b) + " is greatest!\n")
    else:
        print("\n" + str(c) + " is greatest!\n")

greatest_of_three(a, b, c)
