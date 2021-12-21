string1 = "Hello, this string is being used to find double  spaces."

d = string1.find("  ")
if d!=-1:
    print("Double Spaces Found")
else:
    print("Double Spaces NOT Found")