inFile = open('classgrades.txt','r')#Opens the file for grades and reads it
inFile.close()#Closes the file
outFile = open('classscores.txt','w')#Opens a new file to write in

for line in inFile:#Takes each line in the classgrades
    
    grades = []#Makes an empty list for the grades of each student - will soon contain integers
    average = 0#Makes a variable for the average grades of each student
    
    line = line.split()#Splits line into the name and grades(into a list)
    
    for wordsOrNums in line:#Takes each word or number in the line
        
        if wordsOrNums[0] in '1234567890':#If it is a number
            grades.append(wordsOrNums)#Add the number to the empty list
            
        else:#If it is a word
            name = wordsOrNums#Save the name to a variable
    for eachGrade in grades:#Takes each grade in the list of grades
        average = average + int(eachGrade)#Takes the sum of the grades for the average
        
    average = str(average//len(grades))#Finalizes average by dividing by amount of grades - converts to string for writing
    outFile.write(name+' '+average+'\n')#Writes name, space, the average, and a new line in the classscores file
    
outFile.close()#Closes the file we wrote in when done.
