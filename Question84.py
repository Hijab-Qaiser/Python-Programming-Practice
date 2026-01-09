#Create a 5x5 2D array. Calculate the sum of elements in the main diagonal (where row index equals column index).
arr = [
    [1,  2,  3,  4,  5],
    [6,  7,  8,  9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
] #integer array
sum = 0 #integer variable
for row in range(5):
    for column in range(5):
        if row == column:
            sum = sum + arr[row][column]
            break
print(f"Sum of elements in the main diagonal of array = {sum}")

