def getGrade(obtainedMarks):
    if obtainedMarks >= 90:
        return 'A'
    elif obtainedMarks >= 80:
        return 'B'
    elif obtainedMarks >= 70:
        return 'C'
    elif obtainedMarks >= 60:
        return 'D'
    elif obtainedMarks >= 50:
        return 'E'
    else:
        return 'F'    
        
def getGradePoint(grade):
    if grade == 'A':
        return 4.0
    elif grade == 'B':
        return 3.0
    elif grade == 'C':
        return 2.5
    elif grade == 'D':
        return 2.0
    elif grade == 'E':
        return 1.0
    else:
        return 0.0
    

totalCourses = 3
obtainedMarks = []
grades = []
gradePoints = []

for i in range(totalCourses):
    marks = float(input(f"Enter your Obtained Marks for course {i+1}: "))
    obtainedMarks.append(marks)

i = 0
while i < totalCourses:
    grade = getGrade(obtainedMarks[i])
    point = getGradePoint(grade)
    grades.append(grade)
    gradePoints.append(point)
    i += 1

i = 0
isContinue = 'Y'
while isContinue == 'Y' or isContinue == 'y':
    print(f"Your Grade is: {grades[i]},\tYour Grade Point is: {gradePoints[i]:.1f}")
    isContinue = input("Do you have another course for print (y/n): ")
    i += 1


