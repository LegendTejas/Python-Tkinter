# TicTacToe Game
from tkinter import *
import random

# Function to handle the next turn of the game
def next_turn(row, column):

    global player

    # Only allow move if the selected button is empty and there is no winner yet
    if buttons[row][column]['text'] == "" and check_winner() is False:

        # If current player is 'x'
        if player == players[0]:
            buttons[row][column]['text'] = player  # Mark the cell with 'x'

            # Check game status after the move
            if check_winner() is False:  # No winner yet → switch turn
                player = players[1]
                label.config(text=(players[1]+" turn"))

            elif check_winner() is True:  # Current player won
                label.config(text=(players[0]+" wins"))

            elif check_winner() == "Tie":  # Game tied
                label.config(text="Tie!")

        # If current player is 'o'
        else:
            buttons[row][column]['text'] = player  # Mark the cell with 'o'

            # Check game status after the move
            if check_winner() is False:  # No winner yet → switch turn
                player = players[0]
                label.config(text=(players[0]+" turn"))

            elif check_winner() is True:  # Current player won
                label.config(text=(players[1]+" wins"))

            elif check_winner() == "Tie":  # Game tied
                label.config(text="Tie!")


# Function to check if there is a winner or a tie
def check_winner():

    # Check rows
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True

    # Check columns
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True

    # Check main diagonal
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True

    # Check anti-diagonal
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True

    # Check for tie (no empty spaces left)
    elif empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "Tie"

    # No winner and spaces still available
    else:
        return False


# Function to check if there are empty spaces on the board
def empty_spaces():

    spaces = 9  # Total 9 cells initially

    # Count remaining empty cells
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1

    # If no spaces left → False, otherwise True
    if spaces == 0:
        return False
    else:
        return True


# Function to reset the game
def new_game():

    global player

    # Randomly choose starting player
    player = random.choice(players)
    label.config(text=player+" turn")

    # Reset all cells to empty and default background
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#F0F0F0")


# ------------------ Tkinter UI Setup ------------------

window = Tk()
window.title("Tic-Tac-Toe")

# Define players
players = ["x", "o"]

# Randomly select who goes first
player = random.choice(players)

# Create 3x3 button grid placeholder
buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

# Display label showing whose turn it is
label = Label(text=player + " turn", font=('consolas', 40))
label.pack(side="top")

# Restart button to reset the game
reset_button = Button(text="restart", font=('consolas', 20), command=new_game)
reset_button.pack(side="top")

# Frame to hold the game board
frame = Frame(window)
frame.pack()

# Create 3x3 grid of buttons for the board
for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('consolas', 40), width=5, height=2,
                                      command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

window.mainloop()