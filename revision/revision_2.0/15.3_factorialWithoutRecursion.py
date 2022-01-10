def factorial_without_recursion(num):
    product = 1
    for i in range(num):
        product = product * (i+1)
    return product

f = factorial_without_recursion(5)
print(f)
