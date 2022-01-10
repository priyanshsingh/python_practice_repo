def factorial_with_recursion(n):
    if n==0 or n==1:
        return 1
    return n * factorial_with_recursion(n-1)

f = factorial_with_recursion(5)
print(f)
