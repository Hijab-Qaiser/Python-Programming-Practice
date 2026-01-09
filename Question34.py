#Ask the user to enter a number. If it's even (divisible by 2 with no remainder), print "Even". Otherwise, print "Odd". Hint: Use the modulus operator % (Research Div And Mod)
Num = int(input("Enter a number "))  #integer variable
match Num % 2 : 
    case 0 :
        print("Even")
    case _:
        print("Odd")    