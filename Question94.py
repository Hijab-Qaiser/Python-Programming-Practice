#Create a function called findLargest that takes an array as parameter and returns the largest element.
arr = [4, 7, 1, 9, 3] #integer array
def findLargest (arr):
    max = float('-inf')
    for x in range(len(arr)):
        if arr[x] > max:
            max = arr[x]
    return max        
print(f"Largest number in array = {findLargest(arr)}")