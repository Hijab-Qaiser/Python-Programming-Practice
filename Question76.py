# Create an array of 6 numbers. Shift all elements one position to the right (last element becomes first).
number = [5, 3, 8, 2, 9, 1]  # integer array
k = int(input(f"Enter how many times to do circular right shift "))
for y in range(k):
    temp = number[len(number) - 1]
    for x in range(len(number) - 1, 0, -1):
        number[x] = number[x - 1]
    number[0] = temp


print(number)
