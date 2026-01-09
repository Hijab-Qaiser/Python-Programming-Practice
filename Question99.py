#Number Analysis Program-Create a program that:
#Asks the user to enter numbers until they enter -999
#Stores all numbers in an array
#Creates functions for: 
#Finding the sum
#Finding the average
#Finding the largest
#Finding the smallest
#Counting positive and negative numbers
#Prints all analysis results


#module 1
arr = [] #integer array
num= 0 #integer variable 
count = 1 #integer variable
avg = 0 #integer variable
GrandSum = 0 #integer variable
GrandAverage = 0 #integer variable
poscount = 0 #integer variable
negcount = 0 #integer variable
total = 0 #integer variable
#module 2
def Sum(total, num):
    return total + num
#module 3
def Avg(GrandSum,length ):
    avg = GrandSum/length 
    return avg
#module 4
def PosNeg(num,poscount,negcount):
    if num >= 0:
        poscount = poscount + 1 
    else :
        negcount = negcount + 1
    return poscount , negcount  
#module 5
def MaxMin(arr):
    max = arr[0]
    min = arr[0]
    for x in range(1,len(arr)):
        if arr[x] > max:
          max = arr[x]
        if arr[x] < min:
          min = arr[x]
    return max , min     

#module 6
while True:
    num = int(input(f"Enter {count} number "))
    if num == -999:
        break 
    arr.append(num)
    total = Sum(total, num)
    GrandSum = total 
    poscount, negcount = PosNeg(num, poscount, negcount)
    count = count + 1
print(f"Array we have in the end = ")
for m in range(len(arr)):
    print(arr[m])
print(f"Analysis results are as followed: ")
print(f"Sum of array = {GrandSum}")
print(f"Average of array = {Avg(GrandSum,len(arr))}")
print(f"Positive number count = {poscount} and Negative number count = {negcount}")
largest, smallest = MaxMin(arr)
print(f"Largest number =  {largest}  and Smallest number {smallest}")




      

         
   

