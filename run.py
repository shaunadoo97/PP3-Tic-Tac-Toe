import random
from colorama import Fore, init

init(autoreset=True)


board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

CURPLAYER = "X"
WINNER = None
GAMERUNNING = True


# Drawing out the board

def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])


    
def player_input(board):
    """Takes the player input and checking if it is Valid.
    Run through different possibilities for invalid input.
    Place choice on board if valid
    """
    while True:
        inp = input(Fore.YELLOW + "Please enter a number between 1 and 9:" + Fore.RESET)

    # Checking that the input is a number
        if not inp.isnumeric():
            print(Fore.RED + "please enter numbers only!")

    # If it is a number, check the number is a valid choice for the board.
        elif int(inp) not in range(1, 10):
            print(Fore.RED + "Please enter a number 1-9!")

    # If it is valid, check that the space is free to choose on the board.
        elif board[int(inp) - 1] != "-":
            print(Fore.RED + "Sorry, a player has already chosen this spot!")
            
    # If all is well with the world, place it and break the loop.
        else:
            board[int(inp) - 1] = CURPLAYER
            break


def checkHorizontal(board):
    """
    Checking for win or tie
    """
    global WINNER
    if board[0] == board[1] == board[2] and board[1] != "-":
        WINNER = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        WINNER = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        WINNER = board[6]
        return True


def checkRow(board):

    global WINNER
    if board[0] == board[3] == board[6] and board[0] != "-":
        WINNER = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        WINNER = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        WINNER = board[2]
        return True


def checkDiag(board):
    global WINNER
    if board[0] == board[4] == board[8] and board[0] != "-":
        WINNER = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        WINNER = board[2]
        return True


def checkTie(board):
    """
    Checking for Tie
    """
    global GAMERUNNING
    if "-" not in board:
        printBoard(board)
        print("It's a tie!")
        GAMERUNNING = False


def checkWin(board):
    """
    Checking for Win
    """
    global GAMERUNNING
    if checkDiag(board) or checkHorizontal(board) or checkRow(board):
        print(f"The Winner is {WINNER}!")
        print(f"Thanks for playing.")
        return True
    else:
        return False

        GAMERUNNING = False


def switchPlayer():
    """
    Switching Player
    """
    global CURPLAYER
    if CURPLAYER == "X":
        CURPLAYER = "O"
    else:
        CURPLAYER = "X"


def computer(board):
    """
    Computer's Turn
    """

    
    while CURPLAYER == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()
while GAMERUNNING:
        printBoard(board)
        player_input(board)
        if checkWin(board):
            break
        checkTie(board)
        switchPlayer()
        computer(board)
        checkWin(board)
        checkTie(board)