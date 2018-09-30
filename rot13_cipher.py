def rot13(string): #Function and parameters
    """Takes a passage and returns the passage where each letter 13 letters away from it's original position"""
    
    lenString = len(string)#Takes the length of the string
    newString = ''#For adding the text
    
    lowerCase = "abcdefghijklmnopqrstuvwxyz" #Lower Case alphabet
    upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    for i in range(lenString):#Repeat for the amount of letters in the string, A.K.A the length of the string
        numLetter = ord(string[i])#Converts the i'th letter to ASCII
        
        if string[i] in lowerCase:#If the letter is lower case...            
            
            if numLetter>=110 and numLetter<=122:#If the letter+13 needs to go back to the start of the alphabet, subtract 13 instead
                newString = newString + chr(numLetter-13)#The new string is the new string along with numString - 13
                
            elif numLetter<=110 and numLetter>=96:#If the letter is from a to n  
                newString = newString + chr(numLetter+13)#Add 13 in ASCII and convert to a letter again
                
                
        elif string[i] in upperCase:#If the letter is upper case...     
            
            if numLetter>=78 and numLetter<=90:#If the letter+13 needs to go back to the start of the alphabet
                newString = newString + chr(numLetter-13)#The new string is the new string along with numLetter - 13
                
            elif numLetter<=78 and numLetter>=65:#If the letter is from A to N
                newString = newString + chr(numLetter+13)#Add 13 in ASCII and convert to a letter again
                
                
        else:#Otherwise, if not a letter...
            newString = newString + string[i]#The newString is the new string along with the same character
            
    return newString#After, return the newString
