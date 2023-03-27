import os
import random
import time

spots = {1 : "1" , 2 : "2" , 3 : "3" ,  4 : "4" , 5 : "5" , 6 : "6" , 7 : "7" , 8 : "8" , 9 : "9"}

spots4 = {1 : "1" , 2 : "2" , 3 : "3" ,  4 : "4" , 5 : "5" , 6 : "6" , 7 : "7" , 8 : "8" , 9 : "9" , 10 : "10" , 11 : "11" , 12 : "12" , 13 : "13" , 14: "14", 15 : "15", 16 : "16"}


# This function introduces the rules of the game Tic Tac Toe 4*4
def intro4():
    print("You choose to play Tic-Tac-Toe on board 4*4")
    print("Hello! Welcome Tic Tac Toe game!")
    print("\n")
    print("Rules:\n"
          "Player 1 and player 2, represented by X and O.\n "
          "Take turns marking the spaces in a 4*4 grid. The player who succeeds in placing "
          "four of their marks in a horizontal, vertical or diagonal row wins.")
    print("\n")
    input("Press enter to continue.")
    print("\n")
    
# This function introduces the rules of the game Tic Tac Toe 3*3
def intro():
    print("You choose to play Tic-Tac-Toe on board 3*3")
    print("Hello! Welcome Tic Tac Toe game!")
    print("\n")
    print("Rules:\n"
          "Player 1 and player 2, represented by X and O.\n "
          "Take turns marking the spaces in a 3*3 grid. The player who succeeds in placing "
          "three of their marks in a horizontal, vertical or diagonal row wins.")
    print("\n")
    input("Press enter to continue.")
    print("\n")

# Configure Varibale of Tic-Tac-Toe board 4*4
def game_board4(spots4):
    board = (f"|{spots4[1]}|{spots4[5]}|{spots4[9]}|{spots4[13]}|\n|{spots4[2]}|{spots4[6]}|{spots4[10]}|{spots4[14]}|\n|{spots4[3]}|{spots4[7]}|{spots4[11]}|{spots4[15]}|\n|{spots4[4]}|{spots4[8]}|{spots4[12]}|{spots4[16]}|")
    print(board)

# Configure Varibale of Tic-Tac-Toe board 3*3
def game_board(spots):
    board = (f"|{spots[1]}|{spots[2]}|{spots[3]}|\n|{spots[4]}|{spots[5]}|{spots[6]}|\n|{spots[7]}|{spots[8]}|{spots[9]}|")
    print(board)

# Configure Symbol global
def symbol():
    symbol_2 = ""
    symbol_1 = input("Which symbol you choose? for X press 1 for O press any other key: ")
    for i in symbol_1:
        # Check which symbol the player choose
        if symbol_1 == '1':
            symbol_1 = "X"
            symbol_2 = "O"
            print("Player 1, you are X.")
        elif symbol_1 == '2':
            symbol_1 = "O"
            symbol_2 ="X"
            print("Player 2, you are O. ")
        else:
            symbol_1 = "X" 
            symbol_2 = "O"
            print("Default, Player 1 is X and play first. ")
    input("Press enter to continue.")
    print("\n")
    return (symbol_1, symbol_2)

# Configure turn check global
def check_turn(turn):
    if turn % 2 == 0:
        return "O"
    else:
        return "X"

# win cases 3*3
def check_for_win(spots):
    # Horizontal Cases
    if        (spots[1] == spots[2] == spots[3]) \
        or    (spots[4] == spots[5] == spots[6]) \
        or    (spots[7] == spots[8] == spots[9]):
        return True      
    # Vertical Cases
    elif      (spots[1] == spots[4] == spots[7]) \
        or    (spots[2] == spots[5] == spots[8]) \
        or    (spots[3] == spots[6] == spots[9]):
        return True
    # Diagonal Cases
    elif      (spots[1] == spots[5] == spots[9]) \
        or    (spots[3] == spots[5] == spots[7]):
        return True
    else: return False
    
# win cases 4*4
def check_for_win4(spots4):
    # Vertical Cases
    if        (spots4[1] == spots4[2] == spots4[3] == spots4[4]) \
        or    (spots4[5] == spots4[6] == spots4[7] == spots4[8]) \
        or    (spots4[9] == spots4[10] == spots4[11] == spots4[12]) \
        or    (spots4[13] == spots4[14] == spots4[15] == spots4[16]) :
        return True      
    # Horizontal Cases
    elif      (spots4[1] == spots4[5] == spots4[9] == spots4[13]) \
        or    (spots4[2] == spots4[6] == spots4[10] == spots4[14]) \
        or    (spots4[3] == spots4[7] == spots4[11] == spots4[15]) \
        or    (spots4[4] == spots4[8] == spots4[12] == spots4[16]) :
        return True
    # Diagonal Cases
    elif      (spots4[1] == spots4[6] == spots4[11] == spots4[16]) \
        or    (spots4[4] == spots4[7] == spots4[10] == spots4[13]) :
        return True
    else: return False

