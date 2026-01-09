#Create a function called linearSearch that takes an array and a search value as parameters. 
# Return the index if found, -1 if not found.
arr = [12, 5, 8, 3, 19, 7, 25, 1, 14, 9, 6, 20, 4, 18, 11] #integer array
search = int(input(f"Enter the value u want to search ")) #integer variable
def linearSearch(arr,search):
    for count in range(len(arr)):
        if search == arr[count]:
            return f"The value {search} was found at index {count}"
    else: return f"-1"    
print(linearSearch(arr,search))    
