#Create a function called countVowels that takes a string 
# returns the count of vowels in it. 
# Make sure to use a sample value and output the result.
word = input(f"Enter a string value ") #string variable
def countVowels(word):
    vowels = 0 #integer variable
    for count in range(len(word)):
        if word[count] == "a" or word[count] == "e" or word[count] == "i" or word[count] == "o" or word[count] == "u" :
           vowels = vowels + 1
    return vowels    
print(f"Number of vowels in the gven string = {countVowels(word)}")   