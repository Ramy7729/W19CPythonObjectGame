class GameBoard:
    def __init__(self):
        # Instance variables that contain the winning position and layout of the maze.
        self.winningRow = 0
        self.winningColumn = 2
        self.board = [
            [" * ", " * ", "   ", " * ", " * ", " * "],
            [
                " * ",
                "   ",
                "   ",
                "   ",
                " * ",
                " * ",
            ],
            [
                " * ",
                "   ",
                " * ",
                " * ",
                "   ",
                " * ",
            ],
            [
                " * ",
                "   ",
                "   ",
                "   ",
                "   ",
                " * ",
            ],
            [" * ", " * ", " * ", " * ", " * ", " * "],
        ]
    # Method to print the layout of the maze.
    def printBoard(self, playerRow, playerColumn):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if i == playerRow and j == playerColumn:
                    print(" P ", end="")
                else:
                    print(self.board[i][j], end="")
            print("")
    # Method to check the players movement.
    def checkMove(self, testRow, testColumn):
        if self.board[testRow][testColumn].find("*") != -1:
            print("Can't move there!")
            return False
        return True

    # TODO
    # Return True if the player is in the winning column and row
    # Return False otherwise

    # Method that compares the players position to determine if they are in the winning position (0,2).
    def checkWin(self, playerRow, playerColumn):
        # Player wins if their position is equal to the winning postion.
        if (playerRow == self.winningRow and playerColumn == self.winningColumn):
            return True
        return False
    

