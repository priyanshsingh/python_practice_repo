def sum1(n):
    if n==1:
        return 1
    return n + sum1(n-1)

num = int(input("Enter a number = "))
result = sum1(num)
print(result)