#Create an array scores = [85, 90, 78, 92, 88]. Find and print the highest score.
scores = [85, 90, 78, 92, 88] #integer array
max = 0 #integer variable
for x in range(5):
    if scores[x] > max:
        max = scores[x]
print(max)        