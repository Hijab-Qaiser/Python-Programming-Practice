#Ask the user to enter two numbers. Print which one is larger, or if they are equal.
Num1 = int(input("Enter first number ")) #integer variable
Num2 = int(input("Enter second number ")) #integer variable
if Num1 > Num2:
    print(f"{Num1} > {Num2}")
elif Num2 > Num1 :
    print(f"{Num2} > {Num1}")   
else : print("Both numbers entered are equal ")    