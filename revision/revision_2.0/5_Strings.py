#Strings in Python
name = "Priyansh"
print(type(name))
print(name[0])
print(name[5])
print(name[2])

#String Slicing
print(name[1:5])
print(name[1:])
print(name[:5])
c = name[-4:-1]
print(c)

#String Slicing with Skip Value
name = "PriyanshIsGood"
d = name[1:8:2]
print(d)