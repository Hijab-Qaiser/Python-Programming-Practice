#Create a 3x3 2D array. Find and print the largest element and its position (row, column).
arr = [
    [2, 4, 6],
    [1, 3, 5],
    [7, 9, 8] 
] #integer array
max = float('-inf') #integer variable
posrow = 0 #integer variable
poscolumn = 0 #integer variable
for row in range(3):
    for column in range(3):
        if arr[row][column] > max:
           max = arr[row][column]
           posrow = row
           poscolumn = column
print(f"Largest element = {max} and is at arrays {posrow} row ,{poscolumn} column")        


