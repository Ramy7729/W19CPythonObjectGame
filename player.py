class Player:
    def __init__(self, intitalRow, initialColumn):
        # Instance variables that contain the player's position in the maze.
        self.rowPosition = intitalRow
        self.columnPosition = initialColumn

    # This method moves the player up.
    # The player's row position is decremented by one.
    def moveUp(self):
        self.rowPosition -= 1
      
    # This method moves the player down.
    # The player's row position is incremented by one.
    def moveDown(self):
        self.rowPosition += 1

    # This method moves the player left.
    # The player's column position is decremented by one.
    def moveLeft(self):
        self.columnPosition -= 1

    # This method moves the player right.
    # The player's column position is incremented by one.
    def moveRight(self):
        self.columnPosition += 1
