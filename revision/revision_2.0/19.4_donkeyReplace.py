keyword = input("Enter a keyword to replace 'donkey': ")

with open("donkey.txt", "r") as f:
    content = f.read()

content = content.replace("donkey", keyword)


with open("donkey.txt", "w") as f:
    f.write(content)
    print("Replacement done successfully!!!")