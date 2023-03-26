# Import functions (definitions) from help file
from helpers import *
#Feature to reset the screen
import os
# Feature of randomize
import random
# Feature of time
import time


# Dictonary for spots in game board
spots = {1 : "1" , 2 : "2" , 3 : "3" ,  4 : "4" , 5 : "5" , 6 : "6" , 7 : "7" , 8 : "8" , 9 : "9"}


# Introduction
intro()

# Values for each game mode loops
playing = ""
ai = ""
bot = ""
# Value for game end
complete = False
# Value for count which player need to play
turn = 0
# Value for invalid move
re_turn = -1

# if state of game mode values
mathod = input("Which game mode you choose?\nFor AI vs. AI mode press 1\nFor Human vs. AI press on 2\nFor Human vs. Human press any other key\nFor quit press q\n")
# if state for AI vs. AI mode
if mathod == "1":
    playing = False
    ai = False
    bot = True
# if state for Human vs. AI mode
elif mathod == "2":
    bot = False
    playing = False
    ai = True
# if state for quit the game
elif mathod == "q":
        ai = False
        playing = False
        bot = False
#Default option, state if all other options negative this positive 
else:
    playing = True
    ai = False
    bot = False
# if game state is Human vs. AI do this While loop if Human vs. AI condition positive
if ai == True:
    print("You choose to play against Ai")
    input("Press enter to continue")
    # Start of while loop if Human vs. AI condition positive
    while ai:
        # Comands to clean the screen + show the new state of board + which player turn every start of turn
        os.system('cls' if os.name == 'nt' else 'clear')
        game_board(spots)
        print("Player " + str((turn % 2) + 1 ) + "'s turn: Pick your spot press q to quit")
        # if state in case of invalid spot check
        if re_turn == turn:
            print("Invalid spot selected, Please try other spot")
        re_turn = turn
        # if condition to check if the upcoming turn is AI turn (player 2, O)
        if turn %2 == 1:
            # if condition to check if spot 5 is available, if not choose
            if  spots[5] == 5:
                choice = int(5)
            # if not true set spot random
            else:
                while True:
                    move = random.randint(1, 9)
                    # Check if the chosen spot is available and in case is available, apply and break 
                    if not spots[move] in ["X","O"]:
                        choice = int(move)
                        break
        # if not AI turn do this
        else:
            # player input for his choice
            choice = input("Type number between 1-9 or to quit write 'q':")
        # Check if player choose to quit the game and if yes out from the loop 
        if choice == "q":
            ai = False
            print(f"You Choose to quit from Tic-Tac-Toe game\nHope to see you back soon")
        # if choose to continue the game check player choice is in valid spot
        elif int(choice) in spots:
                if not spots[int(choice)] in ["X", "O"]:
                    # if valid choice counter of turn is +1
                    turn += 1
                    # check which symbol to present in the choosen spot
                    spots[int(choice)] = check_turn(turn)
                    # Check possible win, if yes break the loop and continue to reasult
                    if check_for_win(spots):
                        ai, complete = False, True
                    # Check for maximum moves
                    if turn > 8:
                        ai = False
    # Out from loop, print the result
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
# if game state is AI vs. AI do this
elif bot == True:
    print("You choose AI vs. AI")
    input("Press enter to coninue")
    # Start of while loop if AI vs. AI condition positive
    while bot:
        # Comands to clean the screen + show the new state of board + which player turn every start of turn
        os.system('cls' if os.name == 'nt' else 'clear')
        game_board(spots)
        print("Player " + str((turn % 2) + 1 ) + "'s turn")
        # Timeout of helf second between turns.
        time.sleep(0.5)
        # if state in case of invalid spot check
        if re_turn == turn:
            print("Invalid spot selected, Please try other spot")
        re_turn = turn
        # if condition to check if the upcoming turn is AI turn (player 2, O)
        if turn %2 == 1:
            # if condition to check if spot 5 is available, if not choose
            if  spots[5] == 5:
                choice = int(5)
            # if not true set spot random
            else:
                while True:
                    move = random.randint(1, 9)
                    # Check if the chosen spot is available and in case is available, apply and break
                    if not spots[move] in ["X","O"]:
                        choice = int(move)
                        break
                # Check player choice is in valid spot
                if not spots[int(choice)] in ["X", "O"]:
                    # if valid choice counter of turn is +1
                    turn += 1
                    # check which symbol to present in the choosen spot
                    spots[int(choice)] = check_turn(turn)
                    # Check possible win, if yes break the loop and continue to reasult
                    if check_for_win(spots):
                        bot, complete = False, True
                    # Check for maximum moves
                    if turn > 8:
                        bot = False
        # if the turn is player 1 (X) turn do this
        else:
            # if condition to check if spot 5 is available, if not choose
            if  spots[5] == 5:
                choice = int(5)
            # if not true set spot random
            else:
                while True:
                    move = random.randint(1, 9)
                    # Check if the chosen spot is available and in case is available, apply and break
                    if not spots[move] in ["X","O"]:
                        choice = int(move)
                        break
                # Check player choice is in valid spot
                if not spots[int(choice)] in ["X", "O"]:
                    # if valid choice counter of turn is +1
                    turn += 1
                    # check which symbol to present in the choosen spot
                    spots[int(choice)] = check_turn(turn)
                    # Check possible win, if yes break the loop and continue to reasult
                    if check_for_win(spots):
                        bot, complete = False, True
                    # Check for maximum moves
                    if turn > 8:
                        bot = False
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
                # Check if the game has ended (if someone won)
                spots[int(choice)] = check_turn(turn)
        # Check possible win, if yes break the loop and continue to reasult
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

    
