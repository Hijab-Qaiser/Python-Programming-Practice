#Ask the user to enter a number. Print the multiplication table of that number (from 1 to 10) in proper format use string concatenation
Num = int(input("Enter a number ")) #integer variable
for count in range(1,11,1):
    print(f"{Num} * {count} = {Num * count}")
    
