file = open("poem.txt", 'r')
data = file.read()
print(data)

keyword = input("Enter the keyword to be found: ")
keywordFound = data.find(keyword)

if keywordFound!=(-1):
    print("\n**********************************************\n")
    print("""Keyword '""" + keyword + """' was first found at index: """ + str(keywordFound))
else:
    print("\n**********************************************\n")
    print("""Keyword '""" + keyword + """' was not found!""")

file.close()