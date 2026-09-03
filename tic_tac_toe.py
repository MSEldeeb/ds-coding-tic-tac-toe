# In this script you can write your code.
# Start by writing all the functions.
# In the last part after if __name__ == "__main__": you can call the functions to play your game.
# If you run `uv run python tic_tac_toe.py` in the command line the game will start. Try it out! ;)

# Function for ... (displaying the board?)
def update_board(broad, player):
    play1 = input(f"player{player}: choose the square bet. 1 to 9: ")
    # TODO check if this square is already selected before
    if(broad[int(play1) - 1] == 0):
        print(f"selected square by player {player} = ", play1)
        broad[int(play1) - 1] = player
    else:
       # TODO : give the player another try
       # play1 = input("This square is already slected, choose another one.")
       print("This square is already slected, choose another one.")
    print(broad)

    return broad


# Function for... (choosing a player?)
def win_condition(broad):
    winning = 0 # player value and 0 is no winner
    # 1st way three consq. are equal and the values are not zero
    sum1 = broad[0] == broad[1] == broad[2]
    sum2 = broad[3] == broad[4] == broad[5]
    sum3 = broad[6] == broad[7] == broad[8]
    if (sum1 == True ):
        winning = broad[0]
    if (sum2 == True ):
        winning = broad[3]
    if (sum3 == True ):
        winning = broad[6]
    # i, i +3, i+ 6 here 1 bet 1 to 3
    sum1 = broad[0] == broad[3] == broad[6]
    sum2 = broad[1] == broad[4] == broad[7]
    sum3 = broad[2] == broad[5] == broad[8]
    if (sum1 == True ):
        winning = broad[0]
    if (sum2 == True ):
        winning = broad[3]
    if (sum3 == True ):
        winning = broad[6]
    # 1, 5, 9 or 3, 5, 7
    sum1 = broad[0] == broad[4] == broad[8]
    sum2 = broad[2] == broad[4] == broad[6]
    if sum1 == True or sum2 == True:
        winning = broad[4]

    return winning


# ... write as many functions as you need


# Tic-tac-toe game
if __name__ == "__main__":
    # Start a new round of Tic-tac-toe
    broad = [0] * 9
    print("inital board = ", broad)
    while win_condition(broad) == 0:
        broad = update_board(broad, 1)
        print("after player1", broad)
        broad = update_board(broad, 2)
        print("after polayer2", broad)

    print("The winner is ", win_condition(broad))
