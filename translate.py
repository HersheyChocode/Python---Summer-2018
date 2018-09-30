def translate():#Defines Function
    '''translate() -> None
    Prompts user to enter dictionary files and input and output files
    Changes words in input file according to the dictionary file
    Write translation in output file'''
    
    dictFileName = input('Enter name of dictionary: ')#Input name of dictionary
    textFileName = input('Enter name of text file to translate: ')#Input name of text file
    outputFileName = input('Enter name of output file: ' )#Input name of output file
    
    translations = open(dictFileName,'r')#Opens, reads and saves dictFileName to variable "translations"
    
    dictionary = {}#Makes an empty dictionary
    
    for line in translations:#For each line in translations
        line = line.replace('|', ' ')#Replace the vertical line with a space
        line = line.split()#Split the line into different words
        
        while len(line)>2:#While the line is longer than two words
            line[1] = line[1]+' '+line[2]#The third word gets added to the second word
            line.pop(2)#The third word gets removed
            
        dictionary[line[0]] = line[1]#Dictionary adds a key(first word in line) and value(second word in line)
        
    text = open(textFileName,'r')#Opens, reads, and saves textFileName to variable "text"
    translatedText = open(outputFileName,'w')#Opens, reads, and saves outputFileName to variable "translatedText"
    
    for line in text:#For each line in text
        line = line.lower()#Convert everything to lowercase
        line = line.split()#Split the line into words
        
        for word in line:#For each word in the line
            
            if word in dictionary:#If the word is in our dictionary
                word = dictionary[word]#Changes word to the value of the word(in dictionary)        
                
            translatedText.write(word+' ')#Writes this word to translatedText, followed by a space for the next word
            
        translatedText.write('\n')#Writes in a new line after finished with translating the current line
        
    translatedText.close()#Closes the translatedText file
    translations.close()#Closes the translations file
    text.close()#Closes the text file
    
translate()#Calls the function
