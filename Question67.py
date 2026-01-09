#Create an array names = ["Ali", "Sara", "Omar", "Hiba", "Zain"]. Ask the user to enter a name. Print whether the name is in the array or not.
names = ["Ali", "Sara", "Omar", "Hiba", "Zain"] #string array
found = False #boolean variable
Name = input("Enter your name ") #string variable
for x in range(len(names)):
    if Name == names[x]:
        print("Name found")
        found = True
        break
if found == False:
    print("Name not found")