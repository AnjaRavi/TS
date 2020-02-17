
# Tic Tac Toe : run on python-3 version which is currently being used. 
# error: if player input is wrongly put then it goes in a loop of asking player input for all valid and invalid inputs
# 1|2|3
# 4|5|6
# 7|8|9

import random
def drawBoard(board):

  # This function prints out the board that it displays with every move. 
  # "board" is a list of 10 strings representing the board (ignoring index 0)

     print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])

     print('-----------')

     print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])

     print('-----------')

     print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])

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

          return 'player1'

      else:

          return 'player2'

 

def playAgain():

      # This function returns True if the player wants to play again, otherwise it returns False.

      print('Do you want to play again? (yes or no)')

      return input().lower().startswith('y')

 

def makeMove(board, letter, move):

      board[move] = letter

 

def isWinner(board, letter):

      # Given a board and a player’s letter, this function returns True if that player has won.

      return ((board[1] == letter and board[2] == letter and board[3] == letter) or # across the top

      (board[4] == letter and board[5] == letter and board[6] == letter) or # across the middle

      (board[7] == letter and board[8] == letter and board[9] == letter) or # across the bottom

      (board[1] == letter and board[4] == letter and board[7] == letter) or # left column

      (board[2] == letter and board[5] == letter and board[8] == letter) or #  middle col

      (board[3] == letter and board[6] == letter and board[9] == letter) or #  right col

      (board[3] == letter and board[5] == letter and board[7] == letter) or # diagonal

      (board[1] == letter and board[5] == letter and board[9] == letter)) # diagonal

 

def getBoardCopy(board):

      # Make a duplicate of the board list and return it the duplicate.

      # make a dupeBoard list 
      dupeBoard = []

 

      for i in board:

          dupeBoard.append(i)

      return dupeBoard

 

def isSpaceFree(board, move):

      # Return true if the passed move is free on the passed board.

      return board[move] == ' '

 
def getPlayerMove(turn, board):

      # Let the player type in their move.
      # 'turn' stands for player1 turn or player2 turn

      move = ' '

      while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):

          
          print(turn + ' what is your next move? Enter a number from : (1 - 9)')

          move = input()
          
          #putting a "if" condition for invalid moves at the end of the function to avoid the interpreter to print this statement if condition is not satisfied

          if move not in '1 2 3 4 5 6 7 8 9'.split() or  not isSpaceFree(board, int(move)):
            print('Please input a valid move')
          

      return int(move)


def isBoardFull(board):

     # Return True if every space on the board has been taken. Otherwise return False.

     for i in range(1, 10):

         if isSpaceFree(board, i):

             return False

     return True



# starting of the game

print('Welcome to Tic Tac Toe!')



while True:

     # Reset the board

     theBoard = [' '] * 10

     playerOneLetter, playerTwoLetter = inputPlayerLetter()

     turn = whoGoesFirst()

     print('The ' + turn + ' will go first.')

     gameIsPlaying = True


     while gameIsPlaying:

        playerLetter = ''
        
        if turn == 'player1':
          playerLetter = playerOneLetter
          
        else:
          playerLetter = playerTwoLetter

        drawBoard(theBoard)

        move = getPlayerMove(turn, theBoard)

        makeMove(theBoard, playerLetter, move)

        if isWinner(theBoard, playerLetter):

            drawBoard(theBoard)

            print('Hooray! '  + turn + ' has won the game!')

            gameIsPlaying = False

        elif isBoardFull(theBoard):
        
          drawBoard(theBoard)
          print('The game is a tie!')
          break

        else:
        
          if turn == 'player1':
            turn = 'player2'
            
          else:
            turn = 'player1'

     if not playAgain():

         break
         
    # output
"""
  D:\>cd D:\python
D:\python>TicTacToeplayers.py
Welcome to Tic Tac Toe!
Player1 - do you want to be X or O?
x
The player1 will go first.
   |   |
-----------
   |   |
-----------
   |   |
player1 what is your next move? Enter a number from : (1 - 9)
1
 X |   |
-----------
   |   |
-----------
   |   |
player2 what is your next move? Enter a number from : (1 - 9)
2
 X | O |
-----------
   |   |
-----------
   |   |
player1 what is your next move? Enter a number from : (1 - 9)
3
 X | O | X
-----------
   |   |
-----------
   |   |
player2 what is your next move? Enter a number from : (1 - 9)
4
 X | O | X
-----------
 O |   |
-----------
   |   |
player1 what is your next move? Enter a number from : (1 - 9)
5
 X | O | X
-----------
 O | X |
-----------
   |   |
player2 what is your next move? Enter a number from : (1 - 9)
6
 X | O | X
-----------
 O | X | O
-----------
   |   |
player1 what is your next move? Enter a number from : (1 - 9)
7
 X | O | X
-----------
 O | X | O
-----------
 X |   |
Hooray! player1 has won the game!
Do you want to play again? (yes or no)
no
D:\python>
"""
