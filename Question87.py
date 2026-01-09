#Create a function called calculateArea that takes length and width as parameters 
# returns the area of a rectangle. 
# #Make sure to use a sample value and output the result.
length = float(input(f"Enter length of rectangle: ")) #integer variable
width = float(input(f"Enter width of rectangle: ")) #integer variable
area = 0 #integer variable
def CalculateArea(length,width):
    area = length * width 
    return area 

print(f"Area of rectangle = {CalculateArea(length,width)}")
    
