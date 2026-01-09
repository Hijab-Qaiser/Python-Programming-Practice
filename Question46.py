#Ask the user to enter 8 numbers. Count and print how many are greater than 50.
Greater = 0 #integer variable
for count in range(1,9,1):
    Num = int(input(f"Enter {count} Number "))
    if Num > 50:
        Greater = Greater + 1
print(f"total {Greater} numbers entered were greater than 50")        
