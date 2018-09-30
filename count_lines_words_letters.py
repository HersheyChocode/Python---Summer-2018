def get_data(filename):
    '''get_data(filename) -> (int,int,int)
    returns (# of lines,# of words,# of chars) in filename'''
    # add your code here
    inFile = open(filename, 'r')
    fileString = inFile.read()
    numberOfLines = 0
    for line in inFile:
        numberOfLines+=1
    numberOfWords = len(fileString.split())
    numberOfLetters = len(fileString)
    return (numberOfLines, numberOfWords, numberOfLetters)
