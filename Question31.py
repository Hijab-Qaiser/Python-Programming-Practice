# Ask the user to enter a number. If it's positive, print "Positive". If it's negative, print "Negative". If it's zero, print "Zero".
Number = int(input("Enter a number "))  # integer variable
if Number > 0:
    print("positive")
elif Number < 0:
    print("Negative")
else:
    print("Zero")
