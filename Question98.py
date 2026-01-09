#Student Grade System-Create a program that:
#Asks for the number of students
#For each student, asks for 5 subject marks
#Stores all marks in a 2D array
#Creates a function to calculate average
#Creates a function to assign grade based on average: 
#90+: A
#80-89: B
#70-79: C
#60-69: D
#Below 60: F
#Prints each student's average and grade


#module 1
Number_of_student = int(input("Enter number of students in the class ")) #integer variable

#module 2
def average(sum):
    return sum/5
#module 3 
def grades(avg):
    grade = " " #string variable
    match avg:
        case x if x > 90:
            grade = "A"
        case x if x > 80 and x < 89:
            grade = "B"
        case x if x > 70 and x < 79:
            grade = "C"
        case x if x > 60 and x < 69:
            grade = "D"
        case x if x < 60:
            grade = "F" 
    return f"Grade = {grade}" 


#module 4 
arr = []  #2d array (integer and string)
for row in range(Number_of_student):
    count = 1 #integer variable
    marks = 0 #integer variable
    sum = 0 #integer variable
    avg = 0 #integer variable
    student_name = " " #string variable
    new_row = [] #array (integer and string)
    student_name = input(f"Enter student name: ")
    new_row.append(student_name)
    for column in range(5):
        marks = int(input(f"Enter {count} subject marks "))
        count = count + 1
        new_row.append(marks)
        sum = sum + marks
    arr.append(new_row)
    avg = average(sum)

    #module 5
    print(f"Average marks of {student_name} = {avg} ")
    print(grades(avg))
for x in range(len(arr)):
    print(arr[x])

