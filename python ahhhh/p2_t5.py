# 5

def grade():
    marks = []
    for i in range(1, 7):
        mark = int(input("Enter the marks for subject " + str(i) + ": "))
        if mark > 100:
            print("Error: Marks cannot exceed 100.")
            return
        marks.append(mark)
    
    average = sum(marks) / 6
    print("Average Marks:", average)
    
    if average >= 90:
        print("Grade: A")
    elif average >= 80:
        print("Grade: B")
    elif average >= 70:
        print("Grade: C")
    elif average >= 60:
        print("Grade: D")
    else:
        print("Grade: F")

grade()