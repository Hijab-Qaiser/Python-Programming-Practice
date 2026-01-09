#Create an array of 6 numbers. Print the average of all numbers.
numbers = [1,2,3,4,5,6] #integer array
sum = 0 #integer variable
for x in range(6):
    sum = sum + numbers[x]
print(f"Average = {sum/6}")    