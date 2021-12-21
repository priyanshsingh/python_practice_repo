story = "Once upon a time there lived a boy, in the city of Chandigarh. Composing music and playing instruments was his hobby"

print("\n")
print(len(story))                  # Counts the total number of characters in the string

print("\n")
print(story.endswith("hobby"))     # Returns a boolean value, after checking whether the string ends with the entered value or NOT
print(story.endswith("his"))
print(story.endswith("his hobby"))
print(story.endswith("his Hobby"))

print("\n")
print(story.count("Chandigarh"))   # Totol number of occurance of any character in the given string

print("\n")
print(story.capitalize())          # Capitalise the string
print(story.upper())               # UPPPER cases the string
print(story.lower())               # lower cases the string

print("\n")
print(story.find("Chandigarh"))    # Returns the index value where the entered value is found first in the string

print("\n")
print(story.replace("Chandigarh", "Bareilly")) # Replaces the first argument with the second one everywhere the former is found in the string

print("\n")
story = "Once upon a time there lived a boy, in the city of Chandigarh.\nComposing music and playing instruments was his hobby"
print(story)

