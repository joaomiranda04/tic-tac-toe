# tic-tac-toe 

import random # Python function that generates random numbers

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"] # Empty slots for the game board 
currentPlayer = "X" # Player "X" starts the game
winner = None # The winner is None until changed
gameRunning = True # Current state of the game
position = 0

# print the game board
def printBoard(board):
    if gameRunning == True:
        print(board[0] + " | " + board[1] + " | " + board[2])
        print("---------")
        print(board[3] + " | " + board[4] + " | " + board[5])
        print("---------")
        print(board[6] + " | " + board[7] + " | " + board[8])

# take player input
def playerInput(board):
    global inp
    if gameRunning == True:
        print("------------------")
        print()
        inp = int(input(f"Player {currentPlayer} enter a number 1-9: "))
        print()
        if inp >= 1 and inp <= 9 and board[inp-1] == "-": # Checks if the number inserted by the user is valid and if that slot is empty
            board[inp-1] = currentPlayer # inp-1 due to the board array starting with 0
        else:
            print()
            print("Oops a player is already in that spot!")
            exit()
        

# check for win or tie 
def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True
    
def checkVertical(board):
    global winner 
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

def checkTie():
    global gameRunning
    if not(checkHorizontal(board)) and not(checkVertical(board)) and not(checkDiag(board) and "-" not in board):
        if "-" not in board:
            print("It's a tie.")
            print()
            printBoard(board)
            print()
            winner != None
            gameRunning = False
        
def checkWin():
    global gameRunning
    if checkDiag(board) or checkHorizontal(board) or checkVertical(board):
        print(f"The WINNER is player {winner}!")
        print()
        printBoard(board)
        print()
        winner != None
        gameRunning = False
        
# switch the player 
def switchPlayer():
    global currentPlayer
    global inp
    if gameRunning == True:
        if currentPlayer == "X":
            print("------------------")
            print("current player: " + currentPlayer)
            print(f" -> Player {currentPlayer} entered the number {inp}.")
            print("------------------")
            currentPlayer = "O"
        else:
            print("------------------")
            print("current player: " + currentPlayer)
            print(f" -> Player {currentPlayer} entered the number {position+1}.")
            print("------------------")
            currentPlayer = "X"

# computer
def computer(board):
    if gameRunning == True:
        while currentPlayer == "O":
            global position
            position = random.randint(0, 8)
            if board[position] == "-":
                board[position] = "O"
                print()
                switchPlayer()

# check for win or tie again
        
while gameRunning == True:
    print()
    print("Game Running...")
    print()
    if winner == None:
        printBoard(board)
        print()
        playerInput(board)
        checkWin()
        checkTie()
        if winner != None:
            print("Game ended.")
            print("------------------")
            break
        switchPlayer()
        computer(board)
        checkWin()
        checkTie()
    elif winner != None:
        print("Game ended.")
        print("------------------")
        break