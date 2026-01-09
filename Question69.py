#Create an empty array. Ask the user to enter 5 names and add each name to the array using append(). Print all names.
names = [] #string array
for x in range(5):
    name = input(f"Enter {x+1} name ")
    names.append(name)
for y in range(5):
    print(names[y])    
