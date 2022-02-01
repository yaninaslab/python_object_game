

class Player:
    def __init__(self, intitalRow, initialColumn):
        self.rowPosition = intitalRow
        self.columnPosition = initialColumn

    # TODO
    def moveUp(self):
        self.columnPosition = self.columnPosition
        self.rowPosition = self.rowPosition - 1

    # TODO
    def moveDown(self):
        self.columnPosition = self.columnPosition
        self.rowPosition = self.rowPosition + 1

    # TODO
    def moveLeft(self):
        self.columnPosition = self.columnPosition - 1
        self.rowPosition = self.rowPosition

    # TODO
    def moveRight(self):
        self.columnPosition = self.columnPosition + 1
        self.rowPosition = self.rowPosition
