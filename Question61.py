#Ask the user to enter their full name (first and last name separated by space). Print only their last name.
count = 0 #integer variable
fullName = input(f"Enter your full name ") #string variable
for count in range(len(fullName)):
    if fullName[count] == " ":
        print(f"Name entered has a last name :" , fullName[count: len(fullName)])
        break 
    

 
