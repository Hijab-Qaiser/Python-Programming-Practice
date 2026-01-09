# Create an array of 10 numbers. Remove all duplicate values and print the array with unique values only.
numbers = [5, 3, 8, 5, 2, 3, 9, 1, 8, 2]  # integer array
unique = []  # integer array
for x in range(len(numbers)):
    found = False  # boolean integer
    for y in range(len(unique)):
        if numbers[x] == unique[y]:
            found = True
            break
    if found == False:
        unique.append(numbers[x])


print("Unique array : ")
for f in range(len(unique)):
    print(unique[f])


