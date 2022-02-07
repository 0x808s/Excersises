print("Total students is capacity will be 30")

studentList = []
gradeList = []


def mainloop():
    maxStudentList = 30
    while len(studentList) < maxStudentList:
        student = (input("Enter student name: "))
        if not student.isalpha():
            print("Warning: You have invalid characters in the students name.")
        else:
            grades = int(input("Enter students grade: "))
            if grades >= 0 and grades <= 100:
                studentList.append(student)
                gradeList.append(grades)

                print("Current students: ", studentList)
                print("grades: ", gradeList)
            else:
                print("Invalid grade. 0-100")


mainloop()


def average():
    total = sum(gradeList)
    length = len(gradeList)
    averagez = total / length
    print("average grade: ", averagez)


average()
