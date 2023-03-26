import os
import random
import time
spots = {1 : "1" , 2 : "2" , 3 : "3" ,  4 : "4" , 5 : "5" , 6 : "6" , 7 : "7" , 8 : "8" , 9 : "9"}

# This function introduces the rules of the game Tic Tac Toe
def intro():
    print("Hello! Welcome Tic Tac Toe game!")
    print("\n")
    print("Rules:\n"
          "Player 1 and player 2, represented by X and O.\n "
          "Take turns marking the spaces in a 3*3 grid. The player who succeeds in placing "
          "three of their marks in a horizontal, vertical or diagonal row wins.")
    print("\n")
    input("Press enter to continue.")
    print("\n")
    
# Configure Varibale of Tic-Tac-Toe board 
def game_board(spots):
    board = (f"|{spots[1]}|{spots[2]}|{spots[3]}|\n|{spots[4]}|{spots[5]}|{spots[6]}|\n|{spots[7]}|{spots[8]}|{spots[9]}|")
    print(board)

# Configure Symbol
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

# Configure turn check
def check_turn(turn):
    if turn % 2 == 0:
        return "O"
    else:
        return "X"


          
# win cases
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

def game_mathod():
    mathod = input("Do you want to play with friend or with AI?\nFor AI press on 1 for friend press any other key:")
    if mathod == "1":
        playing = False
        ai = True
        return (ai,playing)
    else:
        playing = True
        ai = False
        return (ai,playing)

# Configure turn check
def check_turn_ai(turn):
    if turn % 2 == 0:
        ai_move()
        return "O"
    else:
        return "X"
    
def ai_move():
    if not spots[5] == "5":
        return 5
    
    while True:
        move = random.randint(1, 9)
        if not spots[move] == ["X","O"]:
            return move
        break
    return 5


def bot_game():
    while bot:
        os.system('cls' if os.name == 'nt' else 'clear')
        game_board(spots)
        print("Player " + str((turn % 2) + 1 ) + "'s turn: Pick your spot press q to quit")
        time.sleep(1)
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
                if not spots[int(choice)] in ["X", "O"]:
                    turn += 1
                    spots[int(choice)] = check_turn(turn)
                    if check_for_win(spots):
                        bot, complete = False, True
                    if turn > 8:
                        bot = False
        else:
            if  spots[5] == 5:
                choice = int(5)
            else:
                while True:
                    move = random.randint(1, 9)
                    if not spots[move] in ["X","O"]:
                        choice = int(move)
                        break
                if not spots[int(choice)] in ["X", "O"]:
                    turn += 1
                    spots[int(choice)] = check_turn(turn)
                    if check_for_win(spots):
                        bot, complete = False, True
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


# def friends():
#     # Start of the loop
#     while playing:
        # Reset the screen
#        os.system('cls' if os.name == 'nt' else 'clear')
        # Draw game board + which player turn
#        game_board(spots)
#        print("Player " + str((turn % 2) + 1 ) + "'s turn: Pick your spot press q to quit")
        # Show error about invalid move
#        if re_turn == turn:
#            print("Invalid Spot selected. please try other spot")
        # Get back to the count of the turn
#        re_turn = turn
        # Get input from player
#        choice = input("Type number between 1-9 or to quit write 'q':")
        # Option to quit the game
#        if choice == "q":
#            playing = False
#            print(f"You Choose to quit from Tic-Tac-Toe game\nHope to see you back soon")
        # Check that player input is number from 1-9
#        elif str.isdigit(choice) and int(choice) in spots:
            # Check if the spot is not already taken
#            if not spots[int(choice)] in{"X", "O"}:
                #Valid move, update the board1
#                turn += 1
#                spots[int(choice)] = check_turn(turn)
        # Check if the game has ended (if someone won)
#        if check_for_win(spots): 
#            playing, complete = False, True
#        if turn > 8:
#            playing = False