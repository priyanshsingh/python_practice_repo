def convert(inches):
    return inches * 2.54

inc = int(input("Enter length in inches = "))
result = convert(inc)
print(str(inc) + "inches in centimeters = " + str(result) + " cms")