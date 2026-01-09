#Create a 3x3 2D array and take 9 numbers from the user, store it in the array then Calculate and print the sum of all elements.
arr = [] #integer array
sum = 0 #integer variable
count = 1 #integer variable 
for row in range(3):
    new_row = []
    for column in range(3):
        num = int(input(f"Enter {count} number "))
        count = count + 1
        new_row.append(num)
        sum = sum + num
    arr.append(new_row) 
print(f"Sum of all numbers entered = {sum}")   

for x in range(len(arr)):
    print(arr[x])    