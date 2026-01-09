#Ask the user to enter 10 numbers. Count how many are even and how many are odd. 
even = 0 #integer variable
odd = 0 #integer variable
for count in range(1,11,1):
    Num = int(input(f"Enter {count} number "))
    match Num % 2:
        case 0:
            even = even +1
        case _:
            odd = odd +1
print(f"{even} numbers entered were even and {odd} numbers entered were odd")