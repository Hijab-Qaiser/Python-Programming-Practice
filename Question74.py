#Create an array of 8 numbers. Separate positive numbers into one array and negative numbers into another array. Print both arrays.
numbers = [5, -3, 12, -8, 0, 7, -1, 4] #integer array
pos = [] #integer array
neg = [] #integer array
for x in range(len(numbers)):
    if numbers[x] >=  0:
        pos.append(numbers[x])
    else :
        neg.append(numbers[x])
print("Negative array: ")        
for y in range(len(neg)):
    print(neg[y])
print("Positive array: ")            
for y in range(len(pos)):
    print(pos[y])
