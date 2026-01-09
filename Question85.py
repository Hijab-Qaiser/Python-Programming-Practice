#Create a 3x4 2D array. Calculate and print the sum of each column.
arr = [
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9, 10, 11, 12]
] #integer array
for column in range(4):
    sum = 0 #integer variable
    for row in range(3):
        sum = sum + arr[row][column]
    print(f"Sum of column {column} = {sum}")    
