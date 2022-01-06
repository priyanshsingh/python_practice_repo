num = int(input("ENter a number to find it's factorial = "))

factorial = 1
for i in range(1, num+1):
    factorial = factorial * i
print("Factorial of " + str(num) + " is = " + str(factorial))


    