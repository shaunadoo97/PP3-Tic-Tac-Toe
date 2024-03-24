from helpers import draw_board, check_turn
import os

spots = {1 : '1', 2 : '2', 3 : '3', 4 : '4', 5 : '5', 6 : '6', 7 : '7', 8 : '8', 9 : '9'}


draw_board(spots)

playing = True 
turn = 0

while playing:
    # resets and clears the screen everytime 
    os.system('cls' if os.name=='nt' else 'clear')
    draw_board(spots)
    # Player input
    choice = input()
    if choice == "q":
        playing = False

turn += 1 
spots[int(choice) = check_turn(turn)]