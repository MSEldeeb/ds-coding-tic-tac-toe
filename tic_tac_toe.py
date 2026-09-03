# In this script you can write your code.
# Start by writing all the functions.
# In the last part after if __name__ == "__main__": you can call the functions to play your game.
# If you run `uv run python tic_tac_toe.py` in the command line the game will start. Try it out! ;)

# Function for ... (displaying the board?)

SYMBOLS = {0: " ", 1: "X", 2: "O"}

def display_board(broad):
    """Print the board, showing the square number for empty cells."""
    def cell(i):
        return SYMBOLS[broad[i]] #if broad[i] != 0 else str(i + 1)
 
    rows = [f" {cell(r*3)} | {cell(r*3+1)} | {cell(r*3+2)} " for r in range(3)]
    print("\n" + f"\n{'-' * 11}\n".join(rows) + "\n")

def update_board(broad, player):
    play0 = input(f"player{player}: choose the square bet. 1 to 9: ")

    try:
        play1 = int(play0)
    except:
        print("You lost a try; Choose intgers between 1 to 9")
        return(broad)

    if 0 > play1 or play1 > 9 or type(play1) != int:
        play0 = input(f"player{player}: choose the square bet. 1 to 9 or loss the try: ")
        try:
            play1 = int(play0)
        except:
            print("You lost a try; Choose intgers between 1 to 9")
            return(broad)
    
    if 0 > play1 or play1 > 9 or type(play1) != int:
        print("You lost a try; Choose intgers between 1 to 9")
        return(broad)

    if(broad[int(play1) - 1] == 0):
        print(f"selected square by player {player} = ", play1)
        broad[int(play1) - 1] = player
    else:
       print("This square is already slected, choose another one.")
       broad = update_board(broad, player)
    print(broad)
    return broad

# Function for... (choosing a player?)
def win_condition(broad):
    winning = 0 # player value and 0 is no winner

    lines = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6),             # diagonals
        ]
    for a, b, c in lines:
        if broad[a] == broad[b] == broad[c] and broad[a] != 0:
            winning = broad[a]

    return winning

# ... write as many functions as you need


# Tic-tac-toe game
if __name__ == "__main__":
    # Start a new round of Tic-tac-toe
    broad = [0] * 9
    display_board(broad)
    print("inital board = ", broad)
    while win_condition(broad) == 0:
        broad = update_board(broad, 1)
        print("after player1", broad)
        display_board(broad)
        if win_condition(broad) != 0:
            break;
        broad = update_board(broad, 2)
        print("after polayer2", broad)
        display_board(broad)

    display_board(broad)
    print("The winner is ", win_condition(broad))
