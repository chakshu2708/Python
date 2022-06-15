def replacespace():
    string = input("Enter a sentence: ") #take user input
    newstr = string.replace(" ","-") # replaces all spaces with hyphen
    print(newstr)
    
replacespace()