from itertools import permutations
import time
import json
import math
import copy

#Game is tic tac toe, 4x4 board, players take turn placing a 1 or 2 on ea. square
#player wins by capturing 4 squares, every row and col are used exactly once

nodeCounter = 0


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
    
    # if board does not have exactly 4 rows:
    if len(board) != 4:
        return None
    #     return invalid
    for row in range(0,4):# for each row in board:
        if len(board[row]) != 4:#     if row does not have exactly 4 cells:
            return None #         return invalid

    # # 2. Values
    
    for row in range(len(board)):
        for col in range(0,4):
            if board[row][col] not in (0, 1, 2):
                return None
                
    
    # # 3. Counts
    
    turn = whoseTurn(board)
    # turn = whoseTurn(board)
    if turn == None:
        return None
    
    # # 4. Wins
    oneWon = hasWon(board, 1)
    twoWon = hasWon(board,2)

    if oneWon and twoWon:
        return None
    
    # # 5. The winner must have moved last
    if oneWon and turn != 2:
        return None

    if twoWon and turn != 1:
        return None

    return True

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

    global nodeCounter 
    nodeCounter+=1

    
    #if player 1 at its current position has won
    if hasWon(board, 1):
        return 1 #return 1 and stop
        
    #if player 2 at its current position has won
    if hasWon(board,2):
        return -1
        # return -1 and stop
    
    #if the board is full 
    if not findEmptyCells(board):
        return 0
        #return 0 and stop

    else:
        #otherwise call the miniMax board with its new board, and push
            #player 1 and player 2 to move to their next best possible moves
            #on the board
        player = whoseTurn(board)
        empty = findEmptyCells(board)
        
        if player == 1:
            best = float('-inf')

        if player == 2:
            best = float('inf')


        for row,col in empty:
            newBoard = copy.deepcopy(board)
            #put player into the indexes that newBoard has at the row and col num
            newBoard[row - 1][col - 1] = player
            value = miniMaxRec(newBoard)

            if player == 1 and value > best:
                best = value
            if player == 2 and value < best:
                    best = value
        return best

def miniMaxMods(board):

    #num of nodes expanded
    global nodeCounter 
    nodeCounter = 0

    if not checkValid(board):
        return None
    #who has won? 
    #if player 1 at its current position has won
    if hasWon(board, 1):
        return 1, None, nodeCounter, 0 #return 1 and stop
            
    #if player 2 at its current position has won
    if hasWon(board,2):
        return -1, None, nodeCounter, 0
            # return -1 and stop
        
    #if the board is full 
    if not findEmptyCells(board):
        return 0, None, nodeCounter, 0
        
    

    
    bestMove = None
    #best move for curr player
    currPlayer = whoseTurn(board)
    
    #get the empty spaces return
    empty = findEmptyCells(board)

    if currPlayer == 1:
        best = float('-inf')
    
    if currPlayer == 2:
        best = float('inf')

    
    #timer for cput
    startTimer = time.process_time()
    for row, col in empty:
        newBoard = copy.deepcopy(board)
        newBoard[row - 1][col - 1] = currPlayer
        value = miniMaxRec(newBoard) 

        #if the currplay has a value that is greater than best, set best to val
        if currPlayer == 1 and value > best:
            best = value
            bestMove = (row,col)
        if currPlayer == 2 and value < best:
            best = value
            bestMove = (row,col)
    cpuTimer = time.process_time() - startTimer
    return best, bestMove, nodeCounter + 1, cpuTimer

def readBoard():
    try:
        board = json.loads(input("Enter in your board:"))
        
    except json.JSONDecodeError:
        print("Couldn't read the board")
        return None

    if not isinstance(board,list):
        print("That is not a board")
        return None

    for row in board:
        if not isinstance(row,list):
            print("That is not a board")
            return None

    if not checkValid(board):
        print("The board given isn't valid")
        return None
    
    return board


# function readDepth():
def readDepth():
    try: 
        k = int(input("Enter the k depth:"))

    except ValueError:
        print("K must be a positive integer ")
        return None

    if k <= 0:
        print("k must be a positive integer")
        return None

    return k



# function printBoard(board):
def printBoard(board):
    for row in board:
        print(*row)
    print()


# function readMove(board):
def readMove(board):
    try: 
        text = input("Enter row and column number:")
        row, col = text.split(",")
        row = int(row)
        col = int(col)

    except ValueError:
        print("Enter a move like 2,3")
        return None

    if not (1 <= row <=4 and 1 <= col <= 4):
        print("Row and column must be between 1 and 4")
        return None
    if board[row - 1][col - 1] != 0:
        print("That cell is taken")
        return None
    return (row, col)

# function announceOutcome(board):
def announceOutcome(board):
    if hasWon(board, 1):
        print("Player 1 wins")
    elif hasWon(board, 2):
        print("Player 2 wins")
    else:
        print("The game is a draw")

# function playGame(board, human, computer, k):
def playGame(board, human, computer, k):
    printBoard(board)

    while True:
        if hasWon(board,1) or hasWon(board, 2) or not findEmptyCells(board):
            break

        turn = whoseTurn(board)

        if turn == human:
            move = readMove(board)
            if move is None:
                continue
            row, col = move
            board[row - 1][col - 1] = human
        else:
            value, bestMove, nodes, cpuTime = MinimaxAlphaBetaCutOff(board,k)
            row, col = bestMove
            board[row - 1][col - 1] = computer
            print("Computer plays", bestMove)

        printBoard(board)
    announceOutcome(board)


def main():


    while True:
        choice = input('\nPick one of the options below: \n'
                ' (0) New Game, see board after each play & game outcome\n'
                ' (1) MiniMax results: value, best move, nodes expanded, and CPU time \n'
                ' (2) Board value: the best move for root player\n'
                ' (3) Side by side results of Minimax Cutt Off and MiniMax Alphabeta Cutt Off\n'
                ' (4) Board at each turn and who wins the game\n'
                ' (5) Exit\n').strip()
    
        

        if choice == "0":
            board = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]

            answer = input("Do you want to play first?: (y/n)")
            if answer not in ("y", "n"):
                print("Error try again")
                continue
            
            if answer == "y":
                human = 1
                computer = 2
            else: 
                human = 2
                computer = 1

            k = readDepth()
            if k is not None:
                playGame(board, human, computer, k)
        elif choice == "1":
            
            answer = readBoard()
            if answer is None:
                #go back to the menu
                continue
            else:
                value, bestMove, nodes,cpuTime = miniMaxMods(answer)
                print("Value:", value)
                if bestMove is None:
                    print("Best move: none (the game is over)")

                else:
                    print("Best move:", bestMove)
                print("Nodes expanded:", nodes)
                print("CPU time:", cpuTime)
        elif choice == "2":
            board = readBoard()

            if board is not None:
                k = readDepth()
                if k is not None:
                    value, bestMove, nodes, cpuTime = MinimaxAlphaBetaCutOff(board,k)
                    print("Value:", value )
                    print("Best move:", bestMove)
                    print("Nodes expanded:", nodes)
                    print("CPU time:", cpuTime)
        

        elif choice == "3":
            board = readBoard()
            if board is not None:
                k = readDepth()
                if k is not None:
                    value1, bestMove1, nodes1, time1 = MinimaxCutOff(board,k)
                    value2, bestMove2, nodes2, time2 = MinimaxAlphaBetaCutOff(board,k)
                    print("\nMinimax cutoff (k =", k, "):")
                    print("  Value:", value1)
                    print("  Best move:", bestMove1 if bestMove1 is not None else "none (the game is over)")
                    print("  Nodes expanded:", nodes1)
                    print("  CPU time:", time1)

                    print("\nAlpha-beta cutoff (k =", k, "):")
                    print("  Value:", value2)
                    print("  Best move:", bestMove2 if bestMove2 is not None else "none (the game is over)")
                    print("  Nodes expanded:", nodes2)
                    print("  CPU time:", time2)

                    if value1 == value2 and bestMove1 == bestMove2:
                        print("\nBoth searches agree on the value and the best move.")
                    else:
                        print("\nWarning: the two searches disagree.")
        elif choice == "4":
            board = readBoard()
            if board is None:
                continue
            choice2 = input("Select 1 or 2:")
            if choice2 not in ("1", "2"):
                print("Error detected")
                continue
            human = int(choice2)
            computer = 3 - human

            k = readDepth()
            if k is not None:
                playGame(board, human, computer, k)

        elif choice == "5":
            print("Goodbye")
            break
        else:
            print("Thats not a valid option, try again")
            



    # #make a board that is 4 by 4 thats a list
    # board = [[0 for i in range(4)]for j in range(4)]

    # #TEST
    # userInput = [[1,1,2,2],[1,2,0,1],[1,0,2,1],[0,1,2,2]]

    # #creating a set of 24 lists winning lists

    # #giving input to the board
    # board = userInput

    # #testing miniMaxMod

    # vals = miniMaxMods(board)
    # print(vals)


    # #option 0: allows user to play with the computer. asks if human
    # #wants to play first.  
    
    
    # #user has asked for option 0, ask for their depth of k

    # #while the tree hasnt been expanded to depth k 
    #     #ask the user to input their next move
    #     #start the game by calling MinimaxAlpha BetaCutoff
    #     #display the board after each turn is made
        
    #     #check if the moves are valid/ if anyone has won
    #         #if someone has won, then report the final board output

if __name__ == "__main__":
    main()