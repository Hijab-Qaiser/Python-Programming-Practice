#Ask the user to enter 10 numbers. Calculate and print their average.
Sum = 0 #integer variable 
for count in range(1,11,1):
    Num = int(input(f"Enter {count} number "))
    Sum = Sum + Num
print(f"Average of the entered numbers = {Sum/10}")
    
