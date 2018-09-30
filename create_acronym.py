def make_acronym(string):
    x = string.split()
    lengthString= len(x)
    y = ''
    for i in range(lengthString):
        words = x[i]
        y = y + words[0]
    return y
