#Create an array of words. Sort them alphabetically using the bubble sort technique. (You can try to solve this code but not compulsory for now.)
#ascending order 
arr = ["m", "a", "k", "z", "c", "f", "q", "b"] #string array 
for y in range(len(arr)):  
    found = False #boolean variable    
    for x in range(0,len(arr)-1,1):
          if arr[x] > arr[x+1]:
                temp = arr[x] #string variable
                arr[x] = arr[x+1]
                arr[x+1] = temp
                found = True
            
    if found == False :
        break         
print("Sorted array = ") 
print(arr)

