#Create an array of 5 numbers. Print the sum of all numbers in the array.
numbers = [1 , 2 , 3 , 4 , 5] #integer array
sum = 0 #integer variable
for x in range(5):
    sum = sum + numbers[x]
print(sum)    