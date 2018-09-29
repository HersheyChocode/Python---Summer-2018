playerX = str(input("Player X, enter your name: ")) #Input name for player x
playerO = str(input("Player O, enter your name: ")) #Input name for player y

def make_gameBoard(board): #Function to create a game board
        nums = '\n0 1 2 3 4 5 6' #The numbers that go on top
        gameBoard = '' #Intial empty game goard
        for line in board: #For each line in the board
                for char in line: #For each character in the line
                       gameBoard+=char #Add the character to the gameboard
        gameBoard = nums+gameBoard #Adds the numbers on top of the game board
        print(gameBoard) #prints gameboard
        return(gameBoard)#returns gameboard
    
def turnX(board):
        xColumn= int(input(playerX+" you are X. What column do you want to play in?")) # Input of wanted column
        while xColumn>6 or xColumn<0: #While the input is out of range
                xColumn = int(input("Please enter a valid answer: ")) #New input
        for row in range(5,-1,-1): #For loop for row from 5 to 0
                if board[row][xColumn]=='. ': #If the row'th row and the wanted column is a dot...
                        board[row][xColumn]='X ' # change it to an X
                        return board #Return this board
                if board[row][xColumn]=='\n. ': #If it is a new line dot
                        board[row][xColumn]='\nX ' #Make it a new line X
                        return board #Return this board
        return 'none' #If all are taken up, return none
    
def turnO(board):
        oColumn= int(input(playerO+" you are O. What column do you want to play in?")) # Input of wanted column
        while oColumn>6 or oColumn<0: #While the input is out of range
                oColumn = int(input("Please enter a valid answer: ")) #New input
        for row in range(5,-1,-1): #For loop for row from 5 to 0
                if board[row][oColumn]=='. ': #If the row'th row and the wanted column is a dot...
                        board[row][oColumn]='O ' #change it to an O
                        return board #Return this board
                if board[row][oColumn]=='\n. ': #If it is a new line dot
                        board[row][oColumn]='\nO ' #Make it a new line O
                        return board #Return this board
        return 'none' #If all are taken up, return none
    
def vertical_possibilities(board): #Function for checking if a vertical line won
        for char in range(7): #for loop for six times
                check = '' # Empty string for the character of each column
                for rows in range(6): #For loop for five times
                    check = check + (board[rows][char]).strip('\n') # Adds the char'th value of the row
                if 'X X X X' in check: # If the list has 4 X's in a row
                    return 'X' #Return X
                elif 'O O O O' in check: #If the list has 4 O's in a row
                    return 'O' #Return O
        return 'none' #If nothing is possible, return none
    
def horizontal_possibilities(board): #Function for checking if a horizontal line won
        for row in board: # For the row in board
                check = '' #Creates empty string
                for char in row: #For the character in the row
                        check = check+char #Adds the character to the string
                if 'X X X X' in check: #If there are 4 X's in a row
                        return 'X' #Return X
                elif 'O O O O' in check: #If there are 4 O's in a row
                        return 'O' #Return O
        return 'none'# If nothing is possible, return none
    
def left_diagonal_possibilities(board): #Function for checking the left diagonal possibilities
        for row in range(3): #For loop in range 3
                for column in range(3,7): #For loop in range 3 to 6
                        check = '' #Emtpy string 
                        for nextIncrement in range(4): #For loop in range 4
                                check = check+(board[row+nextIncrement][column-nextIncrement]).strip('\n') #Adds the diagonal character
                        if 'X X X X' in check: #If there are 4 X's in a row
                                return 'X' #Return X
                        elif 'O O O O' in check: #If there are 4 O's in a row
                                return 'O' #Return O
        return 'none' #If nothing is possible, return none
    
def right_diagonal_possibilities(board): #Function for checking the right diagonal possibilities
        for row in range(3): #For loop in range 3
                for column in range(4): #For loop in range 4
                        check = '' #Emtpy string 
                        for nextIncrement in range(4): #For loop in range 4
                                check = check+(board[row+nextIncrement][column+nextIncrement]).strip('\n') #Adds the diagonal character
                        if 'X X X X' in check: #If there are 4 X's in a row
                                return 'X' #Return X
                        elif 'O O O O' in check: #If there are 4 O's in a row
                                return 'O' #Return O
        return 'none' #If nothing is possible, return none
    
rowDots0 = ['\n. ','. ','. ','. ','. ','. ','. '] #First row of dots
rowDots1 = ['\n. ','. ','. ','. ','. ','. ','. '] #Second row of dots
rowDots2 = ['\n. ','. ','. ','. ','. ','. ','. '] #Third row of dots
rowDots3 = ['\n. ','. ','. ','. ','. ','. ','. '] #Fourth row of dots
rowDots4 = ['\n. ','. ','. ','. ','. ','. ','. '] #Fifth row of dots
rowDots5 = ['\n. ','. ','. ','. ','. ','. ','. '] #Sixth row of dots

#Connect Four Game

board = [rowDots0,rowDots1,rowDots2,rowDots3,rowDots4,rowDots5] #Creates the board with all rows of dots
gameBoard = make_gameBoard(board) #Makes the gameboard with the board

while True: #Repeats until broken
    
        if '. ' not in gameBoard: #If there are no more possibilities
            print("Wow! You guys Tied! Congratulations, and good game!") #Print tie statement
            break #break
            
        board = turnX(board) #Converts player X's turn into a board
        
        if board == 'none': #If the columns has no more space
            print("It seems that this column is taken up; we will hand this turn to", playerO) #Swith to player O's turn
            
        gameBoard = make_gameBoard(board) #Makes the gameboard from player X's turn
        
        rd = right_diagonal_possibilities(board) #Checks for right diagonal possibilities
        ld =left_diagonal_possibilities(board) #Checks for left diagonal possibilities
        v = vertical_possibilities(board) #Checks for vertical possibilities
        h = horizontal_possibilities(board) #Checks for horizontal possibilities
        
        if v=='X' or h=='X' or ld=='X' or rd=='X': #If either one of the possibilities has X winning
                print(playerX, ', you won!') #Print a winning statement
                break #Break the while loop
                
        board = turnO(board) #Converts player O's turn into a board
        
        if board == 'none': #If the column has no more space
            print("It seems that this column is taken up; we will hand this turn to", playerX) #Switch to Player X's turn
            
        gameBoard = make_gameBoard(board) #Makes the gameboard from player Y's turn
        
        rd = right_diagonal_possibilities(board) #Checks for right diagonal possibilities
        ld =left_diagonal_possibilities(board) #Checks for left diagonal possibilities
        v = vertical_possibilities(board) #Checks for vertical possibilities
        h = horizontal_possibilities(board) #Checks for horizontal possibilities
        
        if v=='O' or h=='O' or ld=='O' or rd=='O': #If either one of the possibilities has X winning
                print(playerO, ', you won!') #Print a winning statement
                break #Break the while loop
