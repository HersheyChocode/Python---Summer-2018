def replace_word(filename,oldWord,newWord):
    '''replace_word(filename,word) -> None
    Prints text in filename, replaces oldWord with newWord'''
    # you need to fill in the code
    inFile = open(filename,'r')  # open file
    fileString = inFile.read()   # read entire file into a string
    inFile.close()   # we're done with the file, so we can close it now
    wordList = fileString.split()
    i = 0
    para = ''
    for index in wordList:  # skip through wordList by 5s
        if index==oldWord:
            para = para + ' ' + newWord
        else:
            para = para + ' ' + wordList[i]
        i+=1
    print(para)
