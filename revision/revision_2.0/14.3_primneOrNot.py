num = int(input("Enter a number to check whetehr its Prime or Not: "))
count = 0
for i in range(1, (int(num/2)+1)):
    if num%i==0:
        count += 1
    i+=1
if count<=1:
    print("Number is PRIME")
else:
    print("Number is NOT PRIME")
