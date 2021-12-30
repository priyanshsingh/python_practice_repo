print("\nEnter marks of three subjects out of 100 !!!\n")

a = int(input("Enter marks of subject 1 = "))
b = int(input("Enter marks of subject 2 = "))
c = int(input("Enter marks of subject 3 = "))

percent = (a+b+c)/3

print("Percentage of student is: " + str(percent))

if a>40 and b>40 and c>40 and percent>33:
    print("Student passed!!!\n")
else:
    print("Student failed!!!\n")