
"""
Pritning the Board
"""

theBoard = {'1': ' ' , '2': ' ' , '3': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '7': ' ' , '8': ' ' , '9': ' ' }

def get_Board(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print ('-+-+-')
    print (board['4'] + '|' + board['5'] + '|' + board['6'])
    print ('-+-+-')
    print (board['7'] + '|' + board['8'] + '|' + board['9'])




def main():
    get_Board

