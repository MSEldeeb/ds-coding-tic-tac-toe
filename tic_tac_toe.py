# In this script you can write your code.
# Start by writing all the functions.
# In the last part after if __name__ == "__main__": you can call the functions to play your game.
# If you run `uv run python tic_tac_toe.py` in the command line the game will start. Try it out! ;)

# Function for ... (displaying the board?)
def display_board(board):
    print(board[0], "|", board[1], "|", board[2])
    print("---------")
    print(board[3], "|", board[4], "|", board[5])
    print("---------")
    print(board[6], "|", board[7], "|", board[8])

# Function for... (choosing a player?)
def choose_symbol():
    player1 = input("Player 1, choose X or O: ").upper()

    if player1 == "X":
        player2 = "O"
    else:
        player2 = "X"

    return player1, player2

def get_move():
    position = int(input("Choose a position from 1 to 9: "))
    return position

# ADD check_winner HERE
def check_winner(board, symbol):
    if (
        board[0] == symbol and board[1] == symbol and board[2] == symbol
        or board[3] == symbol and board[4] == symbol and board[5] == symbol
        or board[6] == symbol and board[7] == symbol and board[8] == symbol
        or board[0] == symbol and board[3] == symbol and board[6] == symbol
        or board[1] == symbol and board[4] == symbol and board[7] == symbol
        or board[2] == symbol and board[5] == symbol and board[8] == symbol
        or board[0] == symbol and board[4] == symbol and board[8] == symbol
        or board[2] == symbol and board[4] == symbol and board[6] == symbol
    ):
        return True

    return False

# Tic-tac-toe game
if __name__ == "__main__":
    print("Eldeeb")
    print("Welcome to a new round of Tic-Tac-Toe!")
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    player1_symbol, player2_symbol = choose_symbol()

    turn = 0

    while True:

        if turn % 2 == 0:
            print(f"Player 1's turn ({player1_symbol})")
            current_symbol = player1_symbol
        else:
            print(f"Player 2's turn ({player2_symbol})")
            current_symbol = player2_symbol

        position = get_move()

        if board[position - 1] != " ":
            print("This position is already occupied. Choose another position.")
            continue

        board[position - 1] = current_symbol

        display_board(board)

        if check_winner(board, current_symbol):
            print("You won!")
            break
        turn += 1
