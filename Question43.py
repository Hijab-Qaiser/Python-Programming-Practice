#Ask the user to enter 5 numbers. Calculate and print their sum.
Sum = 0 #integer variable
for count in range(1,6,1):
    Num = int(input(f"Enter {count} number "))
    Sum = (Sum + Num)
print("Sum = ", Sum) 