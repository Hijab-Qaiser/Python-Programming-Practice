#Ask the user to enter positive numbers. Stop when they enter a negative number. Print the sum of all positive numbers entered.
count = 1 #integer variable
Num = 0 #integer variable
Sum = 0 #integer variable
while Num >= 0:
    Num = int(input(f"Enter {count} number "))
    count = count+1
    if Num < 0 :
        break
    else :
     Sum = Sum + Num
print(f"Total = {Sum}")    
