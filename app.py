# Collaborated with Liz for this assignment.

# Importing modules to use them.
from gameboard import GameBoard
from player import Player
# Prints instructions for the player.
print("Welcome to the game!")
print("Instructions: ")
print("To move up: w")
print("To move down: s")
print("To move left: a")
print("To move right: d")

print("Try to get to the end! Good Luck!")
print("-----------------------------")

# Create a new GameBoard called board
# Instance of GameBoard
board = GameBoard()
# Create a new Player called player starting at position 3,2
# Instance of Player.
player = Player(3,2)

# This is the game loop that contains the movement logic.
while True:
    board.printBoard(player.rowPosition, player.columnPosition)
    selection = input("Make a move: ")
  
    #Conditionals with nested if statements which allow the player to move through the gameboard.
    
    if (selection == "w"):
        # This checks to see if the player is moving up.
        if (board.checkMove(player.rowPosition -1, player.columnPosition)):
            # This method moves the player up
            player.moveUp()
    elif (selection == "s"):
        # This checks to see if the player is moving down.
        if (board.checkMove(player.rowPosition +1, player.columnPosition)):
            # This method moves the player down
            player.moveDown()
    elif (selection == "a"):
        # This checks to see if the player is moving left.  
        if (board.checkMove(player.rowPosition, player.columnPosition -1)):
            # This method moves the player left.
            player.moveLeft()
    elif (selection == "d"):
        # This checks to see if the player is moving right.      
        if (board.checkMove(player.rowPosition, player.columnPosition +1)):
            # This method moves the player right.
            player.moveRight()
    else:
        # This prints when a user enters an invalid input.
        print("Invalid input, please try again")
    
    # Check if the player has won, if so print a message and break the loop!
    
    # Player wins if their position is the winning postion.
    if (board.checkWin(player.rowPosition, player.columnPosition)):
        print("You are the winner. YEET!!!")
        # Breaks the loop if the player wins.
        break