def letter_count(inputString):
    '''letter_count(inputString) -> None
    prints alphabetized letter count of letters in inputString'''
    inputString = inputString.split()
    allLetters = []
    letterIndex = {}
    for word in inputString:
        word = word.lower()
        word.split()
        for letter in word:
            if letter not in '!?..':
                allLetters.append(letter)
    allLetters.sort()
    for letter in allLetters:
        if letter not in letterIndex:
            letterCount = allLetters.count(letter)
            letterIndex[letter]=str(letterCount)
    for letter in letterIndex:
        print(letter,':', letterIndex[letter])
