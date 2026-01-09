#Ask the user to guess a secret number (42). Keep asking until they guess correctly. Print how many attempts it took.
Num = 0 #integer variable
count = 0 #integer variable
while Num != 42:
    Num = int(input(f"Guess the number "))
    if Num == 42:
        break
    else : 
        count = count+1
print(f"you took9 {count + 1} attempts to guess the right number")        

   