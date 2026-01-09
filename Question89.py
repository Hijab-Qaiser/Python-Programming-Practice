#Create a function called findMax that takes three numbers as parameters 
# returns the largest one. 
# For testing make sure to input three numbers 32, 1, 43 
# output result with suitable message.
Num1 = int(input(f"Enter 1 number "))#integer variable
Num2 = int(input(f"Enter 2 number "))#integer variable
Num3 = int(input(f"Enter 3 number "))#integer variable
max = 0 #integer variable
def findMax(Num1,Num2,Num3):
    if Num1>Num2 and Num1>Num3:
        max = Num1
    elif Num2>Num1 and Num2>Num3:
        max = Num2
    else:
        max = Num3
    return max 
print(f"Largest amoungst {Num1}, {Num2} and {Num3} is {findMax(Num1,Num2,Num3)}")            

