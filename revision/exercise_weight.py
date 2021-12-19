weight = float(input("Enter your Weight? "))
kg_lbs = input("'K'g or 'L'bs: ")

if kg_lbs == 'k' or kg_lbs == 'K':
    print("Weight in Lbs = " + str(weight * 2.20462))

elif kg_lbs == 'l' or kg_lbs == 'L':
    print("Weight in Kg = " + str(weight * 0.453592))

else:
    print("ENter a valid input")
