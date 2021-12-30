list1 = ['priyansh', 'amit', 'shiv', 'pankaj', 'amritesh', 'vikalp', 'dilip']

name = input("Enter a name = ")
name = name.lower()

if (name in list1):
    print("Yes, the name " + name.title() + " is in the list!")
else:
    print("No, the name is NOT in the list!")