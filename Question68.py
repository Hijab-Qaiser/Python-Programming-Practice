#Create an array of 5 numbers. Count and print how many numbers are greater than the average.
numbers = [23,654,234,6,24] #integer array
sum = 0 #integer variable
avg = 0 #integer variable
count = 0 #integer variable
for x in range(5):
    sum = sum + numbers[x]
avg = sum/5
for y in range(5):
    if numbers[y] > avg:
        count = count+1
print("Numbers greater than average = ", count)        
