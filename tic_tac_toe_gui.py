import tkinter as tk
from tkinter import messagebox
from tic_tac_toe import check_winner


window = tk.Tk()
window.title("Tic-Tac-Toe")


board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
current_symbol = "X"
buttons = []


def button_click(index):
    global current_symbol

    # First check if the selected square is empty
    if board[index] == " ":

        # Put the current symbol into the board
        board[index] = current_symbol

        # Show X or O on the clicked button
        buttons[index].config(text=current_symbol)

        # Check if the current player has won
        if check_winner(board, current_symbol):
            messagebox.showinfo(
                "Winner",
                f"Player {current_symbol} won!"
            )

            # Disable all buttons because the game is finished
            for button in buttons:
                button.config(state="disabled")

            return

        # Change to the next player
        if current_symbol == "X":
            current_symbol = "O"
        else:
            current_symbol = "X"

    # If the square was already selected
    else:
        messagebox.showwarning(
            "Occupied",
            "This square has already been selected. Choose another one."
        )


# Create 9 buttons
for i in range(9):

    button = tk.Button(
        window,
        text=" ",
        width=10,
        height=5,
        command=lambda index=i: button_click(index)
    )

    # Store the button in the buttons list
    buttons.append(button)

    # Calculate the row and column
    row = i // 3
    column = i % 3

    # Put the button into the 3 × 3 grid
    button.grid(
        row=row,
        column=column
    )


# Keep the GUI running
window.mainloop()