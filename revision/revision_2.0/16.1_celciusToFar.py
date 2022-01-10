def convert(c):
    f = (c * 9/5) + 32
    print(str(c) + "degree Celcius in Farenheit = " + str(f))

tempInCelcius = int(input("Enter temperature in Celcius = "))
convert(tempInCelcius)