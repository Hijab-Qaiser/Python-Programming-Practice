#Ask the user to enter numbers until they enter -1. Print the count of numbers entered and their average (excluding the -1).
Num = 0 #integer variable
count = 0 #integer variable
Sum = 0 #integer variable
while Num != -1:
    Num = int(input(f"Enter {count + 1} number "))
    if Num == -1:
        break
    count = count + 1 
    Sum = Sum + Num
print(f"Average of total {count} numbers = {Sum/(count - 1)}")    
