
def percent(marks):
    return ((marks[0] + marks[1] + marks[2] + marks[3])/400)*100
    
marks1 = [45,79,99,48]
percentage1 = percent(marks1)

marks2 = [85,79,98,48]
percentage2 = percent(marks2)

print(percentage1, percentage2)