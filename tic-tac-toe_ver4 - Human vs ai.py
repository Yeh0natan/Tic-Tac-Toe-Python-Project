# Import functions (definitions) from help file
from helpers import *
#Feature to reset the screen
import os
# Feature of AI
import random
import time
# Dictonary for spots in game board
spots = {1 : "1" , 2 : "2" , 3 : "3" ,  4 : "4" , 5 : "5" , 6 : "6" , 7 : "7" , 8 : "8" , 9 : "9"}

# Introduction
intro()

# Because we do not know how many move need to play to win we will use while loop
playing = ""
ai = ""
# Value for game end
complete = False
# Value for count which player need to play
turn = 0
# Value for invalid move
re_turn = -1

mathod = input("Do you want to play with friend or with AI?\nFor AI press on 1 for friend press any other key\nFor quit press q\n")
if mathod == "1":
    playing = False
    ai = True
elif mathod == "q":
        ai = False
        playing = False
else:
    playing = True
    ai = False

if ai == True:
    print("You choose to play agains Ai")
    input("Press enter to continue")
    while ai:
        os.system('cls' if os.name == 'nt' else 'clear')
        game_board(spots)
        print("Player " + str((turn % 2) + 1 ) + "'s turn: Pick your spot press q to quit")
        if re_turn == turn:
            print("Invalid spot selected, Please try other spot")
        re_turn = turn
        if turn %2 == 1:
            if  spots[5] == 5:
                choice = int(5)
            else:
                while True:
                    move = random.randint(1, 9)
                    if not spots[move] in ["X","O"]:
                        choice = int(move)
                        break
        else:
            choice = input("Type number between 1-9 or to quit write 'q':")
        if choice == "q":
            ai = False
            print(f"You Choose to quit from Tic-Tac-Toe game\nHope to see you back soon")
        elif int(choice) in spots:
                if not spots[int(choice)] in ["X", "O"]:
                    turn += 1
                    spots[int(choice)] = check_turn(turn)
                    if check_for_win(spots):
                        ai, complete = False, True
                    if turn > 8:
                        ai = False
    # Out from Loop, Print the result
    os.system('cls' if os.name == 'nt' else 'clear')
    game_board(spots)
    # If was a winner, say who won
    if complete:
        if check_turn(turn) == 'X':
            print("Player 1 Win!")
        else:
            print("Player 2 Win!")
    else:
        #Tie game
        print("No Winner")  
    print("Thanks for playing")
elif playing == True:
    print("You choose to play with friend")
    input("Press enter to continue")
    #symbol
    symbol()
    # Start of the loop
    while playing:
        # Reset the screen
        os.system('cls' if os.name == 'nt' else 'clear')
        # Draw game board + which player turn
        game_board(spots)
        print("Player " + str((turn % 2) + 1 ) + "'s turn: Pick your spot press q to quit")
        # Show error about invalid move
        if re_turn == turn:
            print("Invalid Spot selected. please try other spot")
        # Get back to the count of the turn
        re_turn = turn
        # Get input from player
        choice = input("Type number between 1-9 or to quit write 'q':")
        # Option to quit the game
        if choice == "q":
            playing = False
            print(f"You Choose to quit from Tic-Tac-Toe game\nHope to see you back soon")
        # Check that player input is number from 1-9
        elif str.isdigit(choice) and int(choice) in spots:
            # Check if the spot is not already taken
            if not spots[int(choice)] in{"X", "O"}:
                #Valid move, update the board1
                turn += 1
                spots[int(choice)] = check_turn(turn)
        # Check if the game has ended (if someone won)
        if check_for_win(spots): 
            playing, complete = False, True
        if turn > 8:
            playing = False
    # Out from Loop, Print the result
    os.system('cls' if os.name == 'nt' else 'clear')
    game_board(spots)
    # If was a winner, say who won
    if complete:
        if check_turn(turn) == 'X':
            print("Player 1 Win!")
        else:
            print("Player 2 Win!")
    else:
        #Tie game
        print("No Winner")  
    print("Thanks for playing")
else:
    print("Hope to see you soon")

    
