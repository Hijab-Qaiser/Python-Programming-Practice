#Ask the user to enter 5 numbers. Print how many of them are positive.
positive = 0 #integer variable
for count in range(1,6,1):
    Num = int(input(f"Enter {count} number"))
    if Num > 0:
        positive = positive + 1
print(f"total number of positive numbers entered = {positive}" )
        
        