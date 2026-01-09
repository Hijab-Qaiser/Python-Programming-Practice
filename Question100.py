# Ask the user to enter the number of rows. Print the following centered pyramid pattern (Pattern if rows input 5)
row = int(input("Enter how many rows you want: "))
stars = 1 
r = 0
for r in range(row):
    spaces = row - r -1
    s = 0
    for s in range(spaces):
        print(" ", end="")
        k = 0
    for k in range(stars):
        print("*", end="")
    print()
    stars = stars + 2

