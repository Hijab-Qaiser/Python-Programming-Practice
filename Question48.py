#Ask the user to enter 5 numbers. Find and print the smallest number. 
Num = int(input(f"Enter 1 number "))
min = Num #integer variable
for count in range(2,6,1):
    Num = int(input(f"Enter {count} number "))
    if Num < min:
        min = Num
print(f"Smallest number entered = {min}")     


