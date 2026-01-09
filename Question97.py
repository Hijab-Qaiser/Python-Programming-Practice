#Create a function called reverseArray that takes an array as parameter
#returns a new array with elements in reverse order.
arr = [12, 5, 8, 3, 19, 7, 25, 1, 14, 9, 6, 20, 4, 18, 11] #integer array
def reverseArray(arr):
    reverse_arr = [] #integer array
    for x in range(len(arr) - 1, -1, -1):
        reverse_arr.append(arr[x])
    return reverse_arr
print(f"Array in reverse order: ")
print(reverseArray(arr))    
