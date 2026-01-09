#Create two arrays of 5 numbers each. Create a third array that contains the sum of corresponding elements from both arrays.
num1 = [2,3,4,5,6] #integer array
num2 = [2,3,4,5,6] #integer array
sum = 0 #integer variable
sumarr = [] #integer array
for x in range(5):
  sum = num1[x] + num2[x]
  sumarr.append(sum)
  print(sumarr[x])        
        
        