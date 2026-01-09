#Ask the user to enter 5 numbers. Find and print the largest number.
max = 0 #integer variable 
for count in range(1,6,1):
    Num = int(input(f"Enter {count} number "))
    if Num > max:
        max = Num
print(f"Largest number entered = {max}")        