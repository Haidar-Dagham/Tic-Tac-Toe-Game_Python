from tkinter import *               # Import all tkinter classes and functions for GUI
import random                      # Import random module for randomizing first player

def next_turn(row, column):        # Function to handle the next move based on grid position
    global player                  # Access the global variable 'player'

    if buttons[row][column]['text'] == "" and check_winner() is False:  # If cell is empty and no winner yet
        if player == players[0]:   # If current player is player 1
            buttons[row][column]['text'] = player       # Mark the cell with player's symbol
            if check_winner() is False:                 # If still no winner
                player = players[1]                     # Switch to player 2
                label.config(text=(players[1] + " turn"))  # Update label to show next turn
            elif check_winner() is True:                # If current player won
                label.config(text=(players[0] + " wins"))  # Display win message
            elif check_winner() == "Tie":               # If it's a tie
                label.config(text="Tie!")               # Display tie message

        else:                                           # If current player is player 2
            buttons[row][column]['text'] = player       # Mark the cell
            if check_winner() is False:                 # If still no winner
                player = players[0]                     # Switch to player 1
                label.config(text=(players[0] + " turn"))  # Update label
            elif check_winner() is True:                # If current player won
                label.config(text=(players[1] + " wins"))  # Display win
            elif check_winner() == "Tie":               # If tie
                label.config(text="Tie!")               # Display tie

def check_winner():             # Function to check all win conditions
    for row in range(3):        # Check rows
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="green")  # Highlight winning row
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True         # Return True if row has winner

    for column in range(3):     # Check columns
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="green")  # Highlight winning column
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True         # Return True if column has winner

    # Check main diagonal
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")  # Highlight winning diagonal
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True

    # Check anti-diagonal
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")  # Highlight winning diagonal
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True

    elif empty_spaces() is False:   # If there are no empty spaces and no winner
        for row in range(3):        # Color all buttons yellow to indicate a tie
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "Tie"                # Return tie result

    else:
        return False                # Return False if game should continue

def empty_spaces():                 # Function to check if any empty spaces are left
    spaces = 9                      # Total 9 cells
    for row in range(3):           
        for column in range(3):
            if buttons[row][column]['text'] != "":  # If cell is filled
                spaces -= 1                          # Decrease empty space count

    if spaces == 0:
        return False               # No empty spaces
    else:
        return True                # There are still moves to make

def new_game():                    # Reset game to initial state
    global player
    player = random.choice(players)                 # Randomly pick starting player
    label.config(text=player + " turn")             # Update label for current turn
    for row in range(3):                            
        for column in range(3):
            buttons[row][column].config(text="", bg="#F0F0F0")  # Reset buttons' text and color

# GUI Setup
window = Tk()                                      # Create main application window
window.title("Haidar Dagham's Tic-Tac-Toe Game")                        # Set window title

players = ["x", "o"]                               # List of two players
player = random.choice(players)                   # Choose random player to start

buttons = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]        # Create 3x3 grid initialized with 0s

label = Label(text=player + " turn", font=('consolas', 40))  # Label to display current player's turn
label.pack(side="top")                             # Place label at top

reset_button = Button(text="restart", font=('consolas', 20), command=new_game)  # Button to restart game
reset_button.pack(side="top")                      # Place restart button

frame = Frame(window)                              # Frame to hold buttons grid
frame.pack()                                       # Add frame to window

# Create and place the 3x3 buttons grid
for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('consolas', 40), width=4, height=1,
                                      command=lambda row=row, column=column: next_turn(row, column))  # Each button calls next_turn
        buttons[row][column].grid(row=row, column=column)  # Place button in grid layout

window.mainloop()                                  # Start the GUI event loop
