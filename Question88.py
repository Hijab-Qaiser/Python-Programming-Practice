#Create a function called isEven that takes a number as parameter and returns True if even, False if odd. 
#Make sure to use a sample value and output the result.
num  = int(input(f"Enter the number you want to check ")) #integer variable
flag = False #boolean variable
def isEven (num):
    match num % 2 :
        case 0 :
          flag = True
        case _:
          flag = False
    return flag 
        
print(isEven(num))        