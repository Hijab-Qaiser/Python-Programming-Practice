"""Ask the user to enter a grade (A, B, C, D, or F). Print the corresponding message:
A: "Excellent"
B: "Good"
C: "Average"
D: "Below Average"
F: "Fail"""""
Grade = input("Enter your grade ")  #char variable
match Grade:
    case "A":
        print("Excellent")
    case "B":
        print("Good")
    case  "C":
        print("Average")
             
    case "D":
         print("Below Average")
    case "F":
        print("Fail")
    case _:
        print("Invalid grade")    
            

