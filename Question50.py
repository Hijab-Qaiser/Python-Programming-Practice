#Ask the user to enter 6 numbers. Find both the largest and smallest numbers and print them.
Num = int(input(f"Enter 1 number "))
max = Num #integer variable
min = Num #integer variable
for count in range(2,7,1):
    Num = int(input(f"Enter {count} number "))
    if Num > max:
        max = Num
    if Num < min:
        min = Num
print(f"{min} is the smallest and {max} is the largest number entered")
