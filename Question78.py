# Create an array of 10 numbers. Find and print all numbers that appear more than once.
number = [12, 14, 15, 16, 43, 25, 15, 65, 72, 12, 15, 12, 14, 14]  # integer array
unique = []  # integer array
appeared = []  # integer array

for x in range(len(number)):
    found = False  # boolean variable

    for y in range(len(unique)):
        if number[x] == unique[y]:
            found = True

            flag = False  # boolean variable
            for m in range(len(appeared)):
                if number[x] == appeared[m]:
                    flag = True
                    break
            if flag == False:
                appeared.append(number[x])
                break
    if found == False:
        unique.append(number[x])
print(f"Numbers that appeared more than once are: ")
print(appeared)

