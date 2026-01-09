#Create a function called isPrime that takes a number and returns True if it's a prime number, False otherwise. 
# Make sure to use a sample value and output the result.
num = int(input(f"Enter a number "))# integer variable
def isPrime(num):
    if num == 0  or num == 1:
        return (f"{num} is Neither prime nor composite")
    else:
        for count in range(2,num-1):
            if num % count == 0:
                return (f"False")
    return (f"True")
print(isPrime(num)) 