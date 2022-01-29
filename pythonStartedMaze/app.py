from select import select
import gameboard
import player

print("Welcome to the game!")
print("Instructions: ")
print("To move up: w")
print("To move down: s")
print("To move left: a")
print("To move right: d")

print("Try to get to the end! Good Luck!")
print("-----------------------------")

# TODO
# Create a new GameBoard called board
# Create a new Player called player starting at position 3,2
board = gameboard.GameBoard()
player = player.Player(3, 2)


while True:
    board.printBoard(player.rowPosition, player.columnPosition)
    selection = input("Make a move: ")

    # TODO
    if selection == "a":
        player.moveLeft(player.rowPosition, player.columnPosition)
    elif selection == "d":
        player.moveRight()
    elif selection == "w":
        player.moveUp()
    elif selection == "s":
        player.moveDown()
    else:
        print("Invalid entry")
    # Move the player through the board
    # Check if the player has won, if so print a message and break the loop!
