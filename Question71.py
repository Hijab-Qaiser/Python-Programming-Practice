#Create an array of 10 numbers. Find the second largest number in the array.
max = float('-inf') #integer variable
secondmax = float('-inf')  #integer variable
numbers = [1,2,3,4,5,6,7,8,9,10] #integer array
for x in range(10):
    if numbers[x] > max:
        max = numbers[x]
for y in range(10):
    if numbers[y]>secondmax and numbers[y]<max:
        secondmax = numbers[y]
print(f"second largest number in array = {secondmax}")

