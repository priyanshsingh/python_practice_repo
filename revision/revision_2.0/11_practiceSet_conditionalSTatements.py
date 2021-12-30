a = int(input("Enter number 1 = "))
b = int(input("Enter number 2 = "))
c = int(input("Enter number 3 = "))
d = int(input("Enter number 4 = "))

if a>b and a>c and a>d:
    print("'a' is greatest!!! = " + str(a))
elif b>c and b>d:
    print("'b' is greatest!!! = " + str(b))
elif c>d:
    print("'c' is greatest!!! = " + str(c))
else:
    print("'d' is greatest!!! = " + str(d))

