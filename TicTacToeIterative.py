# Tic Tac Toe : run on python-3 version which is currently being used. 
# error: if player input is wrong then it goes in a loop of asking for valid player input 
# This code works only for Integers
#--------Examples----------
#n=2
# 1|2
# 3|4
#----------------
# n=3
# 1|2|3
# 4|5|6
# 7|8|9

import random
def inputRowsColumns():
    n = '0'
    while int(n) <= 0:
      try:
        n = int(input('Please input a non-zero positive value N for your NxN board:'))
      except ValueError:
        n = '0'
    return int(n)
    

def drawBoard(board):
    rows = len(board)

    for i in range(rows):
        cols = len(board[i])
        for j in range(cols):
            print(' ' + board[i][j] + ' ', end='')
            # Print '|' after all columns except last col
            if (j < cols-1):
              print('|', end='')
        print()
        # Print a line of '----' after all rows except last row
        if (i < n -1):
          for k in range(cols):
            print('----', end='')
          print()



def inputPlayerLetter():
      # This method returns a list with player1 and player2’s letter as the first and second item.

      # Lets the player1 type which letter they want to play.

      # declare the variable to hold input-letter by player1
      letter = ''

      # accept a valid player1 input
      while not (letter == 'X' or letter == 'x' or letter == 'O' or letter == 'o'):

          print('Player1 - do you want to be X or O?')

          letter = input().upper()

          # checking if player1 input is valid or not
          if(letter != 'X' and letter != 'x' and letter != 'O' and letter != 'o'):

              print('Please provide a valid input')
              print('')

            
      # the first element in the list is the player1’s letter, the second is the player2's letter.

      if letter == 'X':

          return ['X', 'O']

      else:

          return ['O', 'X']

 

def whoGoesFirst():

      # This method randomly chooses the player who goes first.

      if random.randint(0, 1) == 0:

          return 'Player1'

      else:

          return 'Player2'

 

def playAgain():

      # This function returns True if the player wants to play again, otherwise it returns False.

      print('Do you want to play again? (yes or no)')

      return input().lower().startswith('y')

 
#this function makes a move based on passed parameters
def makeMove(board, letter, row, col):

      board[row][col] = letter

#decides a winner by checking each row 
def isWinnerRows(board, letter):
  rows = len(board)
  for i in range(rows):
    winner = True
    cols = len(board[i])
    for j in range(cols):
      if board[i][j] != letter:
        winner = False
        break
    if winner:
      return True
  
  return False

#decides a winner by checking each column
def isWinnerCols(board, letter):
  rows = len(board)
  cols = len(board[0])
  for j in range(cols):
    winner = True
    for i in range(rows):
      if board[i][j] != letter:
        winner = False
        break
    if winner:
      return True
  
  return False

#decides a winner by checking the diagonal elements
def isWinnerDiagonal(board, letter):
  n = len(board)
  for i in range(n):
      if board[i][i] != letter:
        return False
  
  return True

#decides a winner by checking the reverse-diagonal elements
def isWinnerReverseDiagonal(board, letter):
  rows = len(board)
  # j starts from the last col of the matrix and goes towards col #0
  j = rows - 1
  for i in range(rows):
      if board[i][j] != letter:
        return False
      j = j-1
  
  return True

#this function returns the winning player.
def isWinner(board, letter):

      # Given a board and a player’s letter, this function returns True if that player has won.

      return isWinnerRows(board, letter) or isWinnerCols(board, letter) or isWinnerDiagonal(board, letter) or isWinnerReverseDiagonal(board, letter)
      

def isSpaceFree(board, row, col):

      # Return true if the passed row and col entry is available on the passed board.

      return board[row][col] == ' '

 
#this helper function lets us decide whether is move is valid or not
def notValidMove(row, col, board):
  n = len(board)
  return (row not in range(1,n+1) and col not in range(1, n+1)) or not isSpaceFree(board, row-1, col-1)


def getPlayerMove(turn, board):

      # Let the player type in their move.
      # 'turn' stands for player1 turn or player2 turn
      row = 0
      col = 0
      n = str(len(board))

      while notValidMove(row, col, board):

          print()
          print(turn + ' what is your next move? Enter values in range : (1 - ' +n+')')

          try:
            row = int(input("Row - "))
            col = int(input("Col - "))
          except ValueError:
            row = 0
            col = 0
          
          #putting a "if" condition for invalid moves at the end of the function to avoid the interpreter to print this statement if condition is not satisfied

          if notValidMove(row, col, board):
            print('Please input a valid move')
          

      return(int(row)-1, int(col)-1)


def isBoardFull(board):

     # Return True if every space on the board has been taken. Otherwise return False.
     rows = len(board)
     for i in range(rows):
        cols = len(board[i])
        for j in range(cols):
         if isSpaceFree(board, i, j):
             return False

     return True



# starting of the game

print('Welcome to Tic Tac Toe!')
print('-----------------------')

while True:

     # Reset the board
    
     n = ''
     n = inputRowsColumns();

     theBoard = [[' ' for x in range(n)] for y in range(n)] 

     drawBoard(theBoard)

     playerOneLetter, playerTwoLetter = inputPlayerLetter()
     print('Player1 letter: ' +playerOneLetter)
     print('Player2 letter: ' +playerTwoLetter)

     turn = whoGoesFirst()
    
     print()
     print(turn + ' will go first.')

     gameIsPlaying = True


     while gameIsPlaying:

        playerLetter = ''
        
        if turn == 'Player1':
          playerLetter = playerOneLetter
          
        else:
          playerLetter = playerTwoLetter

        row, col = getPlayerMove(turn, theBoard)

        makeMove(theBoard, playerLetter, row, col)

        drawBoard(theBoard)

        if isWinner(theBoard, playerLetter):

            drawBoard(theBoard)

            print('Hooray! '  + turn + ' has won the game!')

            gameIsPlaying = False

        elif isBoardFull(theBoard):
        
          drawBoard(theBoard)
          print('The game is a tie!')
          break

        else:
        
          if turn == 'Player1':
            turn = 'Player2'
            
          else:
            turn = 'Player1'

     if not playAgain():

         break
         
    # output
"""
D:\python>TicTacToeIterative.py
Welcome to Tic Tac Toe!
-----------------------
Please input a non-zero positive value N for your NxN board:2
   |
--------
   |
Player1 - do you want to be X or O?
x
Player1 letter: X
Player2 letter: O
Player2 will go first.
Player2 what is your next move? Enter values in range : (1 - 2)
Row - 1
Col - 1
 O |
--------
   |
Player1 what is your next move? Enter values in range : (1 - 2)
Row - 1
Col - 2
 O | X
--------
   |
Player2 what is your next move? Enter values in range : (1 - 2)
Row - 2
Col - 2
 O | X
--------
   | O
 O | X
--------
   | O
Hooray! Player2 has won the game!
Do you want to play again? (yes or no)
yes
Please input a non-zero positive value N for your NxN board:
"""
