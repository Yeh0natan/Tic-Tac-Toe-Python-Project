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
            