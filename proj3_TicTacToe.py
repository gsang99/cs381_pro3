from itertools import permutations
import time
import math

#Game is tic tac toe, 4x4 board, players take turn placing a 1 or 2 on ea. square
#player wins by capturing 4 squares, every row and col are used exactly once


def winningSets():
    sets = [] #stores a winning set
    ordering = [1,2,3,4]
    for n in permutations(ordering): #creating all winning permutations
        cells = []
        for i in range(1,5):
            cells.append((i,n[i - 1] )) #grabbing the row, then the number
        sets.append(cells)
    return sets

#calling once at the top of the file to make it available
WINNING_SETS = winningSets()


#checking which player has won
def hasWon(board,player):
    for winSet in WINNING_SETS: #for each set in winning sets
        allMatch = True #all match  is true
        for row,col in winSet: #for each row and col in set
            if board[row - 1][col - 1] != player:
                allMatch = False
        if allMatch:
            return True
    return False
        

#full boarch check for any empty cells left?
def findEmptyCells(board):
    empty = []
    #search the board for an open space until there are no more
    for row in range(0,4):
        for col in range(0,4):
            if board[row][col] == 0: #if you find an open space
                empty.append((row + 1,col + 1)) #store it in a empty list
    return empty
        
    

#count the 1s and 2s to see who is first
def whoseTurn(board):
    ones = 0
    twos = 0
    for row in range(0,4): # for each row in board:
        for col in range(0,4):#     for each cell in row:
            if board[row][col] == 1:#         if cell is 1:
                ones = ones + 1#             ones = ones + 1
            if board[row][col] == 2:#         if cell is 2:
                twos = twos + 1#             twos = twos + 1

    if ones == twos:# if ones == twos:
        return 1 #     return 1
    if ones == twos + 1: # if ones == twos + 1:
        return 2 #     return 2
    return None # return invalid

def checkValid(board):
    # # 1. Shape
    # if board does not have exactly 4 rows:
    if len(board) != 4:
        return None
    #     return invalid
    for row in range(0,4):# for each row in board:
        if len(row) != 4:#     if row does not have exactly 4 cells:
            return None#         return invalid

    # # 2. Values
    # for each row in board:
    #     for each cell in row:
    #         if cell is not 0, 1, or 2:
    #             return invalid

    # # 3. Counts
    # turn = whoseTurn(board)
    # if turn is None:
    #     return invalid

    # # 4. Wins
    # oneWon = hasWon(board, 1)
    # twoWon = hasWon(board, 2)

    # if oneWon and twoWon:
    #     return invalid

    # # 5. The winner must have moved last
    # if oneWon and turn is not 2:
    #     return invalid
    # if twoWon and turn is not 1:
    #     return invalid

    # return valid
    pass

#rec mini max function
def miniMaxRec(board):
    """
    Input position is U
    Output: val at root
    if (leaf(u) return Eval(u)) no successor, static eval
    if (max-node(u)) val continues to negative infinity, initalize return val for max code
    else val continues pos infinity, initalize return val for min node

    for ea v inside of the Succ(u)
    """
    

    pass

#helper function for mini max
def miniMaxRecHelper():
    pass

#checking if the board is valid
def checkValid(board):
    #copyOfCurrentBoard
    pass
def main():

    #make a board that is 4 by 4 thats a list
    board = [[0 for i in range(4)]for j in range(4)]

    #TEST
    userInput = [[2,1,0,0], [0,1,0,0], [0,0,0,0], [0,0,2,0]]

    #creating a set of 24 lists winning lists

    #giving input to the board
    board = userInput

    #printing the winning sets
    sets = winningSets()
    print(sets)


    #option 0: allows user to play with the computer. asks if human
    #wants to play first.  
    
    
    #user has asked for option 0, ask for their depth of k

    #while the tree hasnt been expanded to depth k 
        #ask the user to input their next move
        #start the game by calling MinimaxAlpha BetaCutoff
        #display the board after each turn is made
        
        #check if the moves are valid/ if anyone has won
            #if someone has won, then report the final board output

    
    pass

if __name__ == "__main__":
    main()