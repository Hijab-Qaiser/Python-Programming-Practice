# Create a function called countOccurrences that takes an array and a value as parameters.
# Return how many times the value appears in the array.
arr = [3, 5, 2, 3, 7, 3, 5, 3, 1, 5] # integer array
search = int(input(f"Enter the value u want to check "))  # integer variable


def countOccurrences(arr, search):
    occured = 0  # integer variable
    for count in range(len(arr)):
        if search == arr[count]:
            occured = occured + 1

    return f"The value {search} was found in index {occured} times"


print(countOccurrences(arr, search))
