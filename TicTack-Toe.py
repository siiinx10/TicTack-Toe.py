#printing the game board
import random
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
currentPlayer = 'X'
winner = None
gameRunning = True

#Board
def print_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("-----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("-----------")
    print(board[6] + " | " + board[7] + " | " + board[8])
print_board(board)


          
#take player input
def playerInput(board):
    input1 = int(input("Enter a number to specif the place on the board:"))
    if input1 >= 1 and input1 <= 9 and board[input1 - 1] == "-":
        board[input1 - 1] = currentPlayer
    else:
        print("choose another place on the board")
#check for win or tie 
def checkHorizontal(board):
    global winner
    if board[0] == board[1] ==board[2] and board[0] != "-":
            winner = board[0]
            return True
    elif board[3] == board[4] ==board[5] and board[3] != "-":
            winner = board[3]
            return True
    if board[6] == board[7] ==board[8] and board[6] != "-":
            winner = board[6]
            return True
        
def checkRow(board):
    global winner
    if board[0] == board[3] ==board[6] and board[0] != "-":
            winner = board[0]
            return True
    elif board[1] == board[4] ==board[7] and board[1] != "-":
            winner = board[3]
            return True
    if board[2] == board[5] ==board[8] and board[2] != "-":
            winner = board[2]
            return True
    
def checkDiagonal(board):
    global winner
    if board[0] == board[4] ==board[8] and board[0] != "-":
            winner = board[0]
            return True
    elif board[2] == board[4] ==board[6] and board[2] != "-":
            winner = board[3]
            return True
    
def checkTie(board):
      global gameRunning
      if "-" not in board:
            printBoard(board)
            print("It is a tie")
            gameRunning = False

def checkWin():
      if checkDiagonal(board) or checkHorizontal(board) or checkRow(board):
            print(f"The winner is {winner}")
#switch playert
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
            currentPlayer = "O"
    

    else:
          currentPlayer = "X"


#A computer bot for tick tak toe
def computer(board):
      while currentPlayer == "O":
            position = random.randint(0,8)
            if board[position] == "-":
                  board[position] = "O"
                  switchPlayer()
#check for win or tie again
while gameRunning:
      print_board(board)
      playerInput(board)
      checkWin()
      checkTie(board)
      switchPlayer()
      computer(board)
      checkWin()
      checkTie(board)
