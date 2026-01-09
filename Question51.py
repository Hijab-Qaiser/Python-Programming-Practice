#Ask the user to enter numbers until they enter 0. Print the sum of all the numbers entered (excluding the 0).
Num = 1 # integer variable 
count = 1 #integer variable
Sum = 0 #integer variable
while Num != 0 :
    Num = int(input(f"Enter {count} number "))
    count = count + 1
    Sum = Sum + Num
print(f"Sum of all {count} entered numbers = {Sum}")

