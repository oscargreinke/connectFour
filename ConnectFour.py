import pdb
from random import *

#BUGS:

def rowCheck(col):
    for i in range(0,5):
        if(Board[i+1][col] != "-"): #goes down the col, checking if the next space is already occupied
            if((i+1) == 0):
                print i
                print "Row full"
                return 6 #so row full has a state
            #print i #debug
            return i
    return 5

def resetBoard():
    for i in range(0,6):
        for j in range(0,7):
            Board[i][j] = "-"
            
    printBoard()

def printBoard():
    print Board[0]
    print Board[1]
    print Board[2]
    print Board[3]
    print Board[4]
    print Board[5]

def computerMove(cSymbol):
    gettingMove = True
    while(gettingMove): #makes sure doesn't pick a full col
        cCol = randint(0,6)
        if(rowCheck(cCol) != 6):
            gettingMove = False
    Board[rowCheck(cCol)][cCol] = cSymbol
    printBoard()
    print "\n"


def playerMove(pSymbol):
    gettingMove = True
    while(gettingMove):
        pCol = int(raw_input("Pick a column 0-6: "))
        while(pCol > 6 or pCol < 0): #checks to make sure it's a valid number TODO: make it not crash with letters
            print "Please input a valid column"
            pCol = int(raw_input("Pick a column 0-6: "))
        confirm = raw_input("Are you sure this is the column you want (y/n)?")
        while(confirm != "y" and confirm != "n"): #checks for valid answer
            print "Please input a valid answer"
            confirm = raw_input("Are you sure this is the column you want (y/n)?")
        if(confirm == "y"): #breaks loop
            gettingMove = False       
    Board[rowCheck(pCol)][pCol] = pSymbol #drops token
    printBoard()
    print "\n"

def checkWin():
    #Board[row][col] Ignore this it's a note
    ###########HORIZONTAL VICTORY############
    victory = 0 #0 = no victory, 1 = victory, 3 = draw
    for i in range(0, 6):
        for j in range(0,7):
            if(Board[i][j] != "-" and j != 6): #Checks for space being same as last and not edge
                if(Board[i][j+1] == Board[i][j] and j+1 != 6): #checks if next space is same as last and not edge
                    if(Board[i][j+2] == Board[i][j] and j+2 != 6): # ""
                        if(Board[i][j+3] == Board[i][j] ): #Checks if next space is same as last
                            victory = 1
 #Debug                           print "horizontal victory"
                            return victory
    ###########VERTICAL VICTORY#############
    for i in range(0, 6): #see above for comments, it's the bloody same but vertical
        for j in range(0,7):
            if(Board[i][j] != "-" and i != 5):
                if(Board[i+1][j] == Board[i][j]  and i+1 !=5):
                    if(Board[i+2][j] == Board[i][j]  and i+2 !=5):
                        if(Board[i+3][j] == Board[i][j] ):
                           victory = 1
 #Debug                          print "vertical victory"
                           return victory
    #########DIAGONAL VICTORY RIGHT+DOWN############
    for i in range(0, 6): 
        for j in range(0,7):
            if(Board[i][j] != "-" and j != 6 and i != 5):
                if(Board[i+1][j+1] == Board[i][j] and j+1 != 6 and i+1 != 5):
                    if(Board[i+2][j+2] == Board[i][j] and j+2 != 6 and i+2 != 5):
                        if(Board[i+3][j+3] == Board[i][j]):
                            victory = 1
 #debug                           print "diagonal victory r"
                            return victory
    #########DIAGONAL VICTORY LEFT+DOWN############
    for i in range(0, 6): 
        for j in range(6,-1,-1): #3rd arg is step size (thx stackoverflow)
            if(Board[i][j] != "-" and j != 0 and i != 5): #Same as previous, just makes the diagonal go left
                if(Board[i+1][(j-1)] == Board[i][j] and j-1 != 0 and i+1 != 5):
                    if(Board[i+2][(j-2)] == Board[i][j] and j-2 != 0 and i+2 != 5):
                        if(Board[i+3][(j-3)] == Board[i][j]):
                            victory = 1
 #debug                           print "diagonal victory l"
                            return victory
    ########DRAW########
    counter = 0
    for i in range(0,6):
        for j in range (0,7):
            if(Board[i][j] != "-"):
                counter += 1
            if(Board[i][j] == "-"):
                counter = 0
    if(counter == 42):
        victory = 3
        return victory
    return victory #Returns 0
            


        
def playGame():
    resetBoard()
    playerOne = raw_input("Should player one be a computer? y/n ") 
    while(playerOne != "y" and playerOne != "n"): #makes sure input is valid character
        print "Please enter a valid chracter"
        playerOne = raw_input("Should player one be a computer? y/n ")
    symbolOne = raw_input("What should player one's symbol be? ") #player one determined, asks for symbol
    if(playerOne == "n"):
        playerTwo = raw_input("Should player two be a computer? y/n ")
        while(playerTwo != "y" and playerTwo != "n"): #same as above but for player 2
            print "Please enter a valid chracter"
            playerTwo = raw_input("Should player two be a computer? y/n ")
        symbolTwo = raw_input("What should player two's symbol be? ") #player 2 determined, asks for symbol
        while(symbolTwo == symbolOne):
            print "Symbol taken"
            symbolTwo = raw_input("What should player two's symbol be? ")
        if(playerTwo == "n"):
            while(True): #plays game w/ 2 humans
                playerMove(symbolOne)
                if(checkWin() == 1):
                    print "Player one victory!"
                    break
                elif(checkWin() == 3):
                    print "Draw!"
                    break
                playerMove(symbolTwo)
                if(checkWin() == 1):
                    print "Player two victory!"
                    break
                elif(checkWin() == 3):
                    print "Draw!"
                    break
        elif(playerTwo == "y"): #plays game w/ 1 human, 1 cpu
            while(True):
                playerMove(symbolOne)
                if(checkWin() == 1):
                    print "Player victory!"
                    break
                elif(checkWin() == 3):
                    print "Draw!"
                    break
                computerMove(symbolTwo)
                if(checkWin() == 1):
                    print "Computer victory!"
                    break
                elif(checkWin() == 3):
                    print "Draw!"
                    break
        
    elif(playerOne == "y"): #player 1 is bot
        playerTwo = raw_input("Should player two be a computer? y/n ")
        while(playerTwo != "y" and playerTwo != "n"): #same as above but for player 2
            print "Please enter a valid chracter"
            playerTwo = raw_input("Should player two be a computer? y/n ")
        symbolTwo = raw_input("What should player two's symbol be? ") #player 2 determined, asks for symbol
        while(symbolTwo == symbolOne):
            print "Symbol taken"
            symbolTwo = raw_input("What should player two's symbol be? ")
        if(playerTwo == "n"):
            while(True): #plays game w/ 2 humans
                computerMove(symbolOne)
                if(checkWin() == 1):
                    print "Computer victory!"
                    break
                elif(checkWin() == 3):
                    print "Draw!"
                    break
                playerMove(symbolTwo)
                if(checkWin() == 1):
                    print "Player victory!"
                    break
                elif(checkWin() == 3):
                    print "Draw!"
                    break
        elif(playerTwo == "y"): #plays game w/ 1 human, 1 cpu
            while(True):
                computerMove(symbolOne)
                if(checkWin() == 1):
                    print "Computer one victory!"
                    break
                elif(checkWin() == 3):
                    print "Draw!"
                    break
                computerMove(symbolTwo)
                if(checkWin() == 1):
                    print "Computer two victory!"
                    break
                elif(checkWin() == 3):
                    print "Draw!"
                    break
            if(raw_input("Play again? y/n ") == "y"):
                playGame()
            else:
                print "k"
    else: #debug
        print "Ya done goofed"
    


Board = [["-", "-", "-", "-", "-", "-", "-"],
         ["-", "-", "-", "-", "-", "-", "-"],
         ["-", "-", "-", "-", "-", "-", "-"],
         ["-", "-", "-", "-", "-", "-", "-"],
         ["-", "-", "-", "-", "-", "-", "-"],
         ["-", "-", "-", "-", "-", "-", "-"]]

playGame()
