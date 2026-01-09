#Create a function called factorial that takes a number and returns its factorial.
# Make sure to use a sample value and output the result.
num = int(input(f"Enter a number for factorial ")) #integer variable
def factorial(num):
    fact = 1 #integer variable
    if num == 0  or num == 1:
        return (f"Factorial = 1")
    else:
        for count in range(num,1,-1):
            fact = fact * count 
        return (f"Factorial = {fact}")
print(factorial(num))
        



