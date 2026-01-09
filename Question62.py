#Create a variable email = "student@school.com". Extract and print only the part before the @ symbol.
email = "student@school.com" #string variable
studentName = " " #string variable
for count in range(len(email)):
    if email[count] == "@" :
        break
    else :
      studentName = studentName + email[count]
print(studentName)     
    