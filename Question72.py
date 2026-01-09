#Create an array of names. Ask the user to enter a name. If found, print its index position. If not found, add it to the array.
names = ["Ali", "Sara", "Omar", "Hiba", "Zain"] #string array
found = False
name = input("Enter a name ") 
for x in range(len(names)):
    if names[x] == name:
        print(f"{name} was found in array at {x} index")
        found = True 
        break
if found == False :
    names.append(name)
    print(f"{name} was not found in array and is now added at {len(names)} position")    