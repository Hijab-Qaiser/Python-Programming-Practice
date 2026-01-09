#Create a 4x5 2D array with student marks (4 students, 5 subjects each). Calculate and print the average marks for each student.
arr = []  #2d array (integer and string)
for row in range(4):
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
    avg = sum/5
    print(f"Average marks of {student_name} = {avg} ")
for x in range(len(arr)):
    print(arr[x])    

