# Create a function called arraySum that takes an array as parameter and returns the sum of all elements.
arr = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
]  # integer variable
def arraySum(arr):
    sum = 0  #integer variable
    for x in range(len(arr)):
        sum = sum + arr[x]
    return sum
print(arraySum(arr))
