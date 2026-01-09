#Create a 4x4 2D array. Fill it with numbers 1 to 16 (row by row). Print the array.
arr = [] #integer array
count = 1 #integer variable
for row in range(4):
    row = []
    for column in range(4):
        row.append(count)
        count = count + 1
    arr.append(row)
for x in range(len(arr)) :
    print(arr[x])

