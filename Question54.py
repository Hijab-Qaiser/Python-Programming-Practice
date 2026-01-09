#Ask the user to enter a password. Keep asking until they enter the correct password "python123".
password = " " #string variable
while password != "python123":
    password = input(f"Enter your password ")
    if password == "python123":
        break 
    else :
        print(f"Wrong password enter it again")