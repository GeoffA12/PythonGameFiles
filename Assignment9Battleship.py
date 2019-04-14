# Assignment 9 Battleship Program
import random
def main():
    global masterBoard
    m = 10
    n = 10
    masterBoard = [['0' for i in range(m)] for j in range(n)]
    print("Welcome to the battleship game.")
    print("Right now, the sea is empty.")
    
    printBoard()
    print("It's your turn to place your ships on the map now.")
    userShips()
    print("Now the computer will place their ships at random locations.")
    computerShips()
    print("Now its time to play the game!")
    playGame()
    
def printBoard():
    global masterBoard
    print()
    print("BOARD")
    print("'\@\' character is your ships.")
    print()
    print("  0123456789")
    for row in range(len(masterBoard)):
        line = "" + str(row) + "|"
        for column in range(len(masterBoard[row])):
            # Hide the computer ships from the board display
            if masterBoard[row][column] == '#':
                line += "0"
            else:
                line += masterBoard[row][column]
        print(line + "|" + str(row))
    print("  0123456789")
    print()

def userShips():
    global masterBoard
    for i in range(5):
        while True:
            try:
                print("Enter two numbers between 0-9 with a space in between")
                x1, y1 = [int(i) for i in input().split()]
                print(x1, y1)
                if (x1 < 0 or x1 > 9):
                    print("Invalid X coordinate. Must be 0-9.")
                    continue
                if (y1 < 0 or y1 > 9):
                    print("Invalid Y coordinate. Must be 0-9.")
                    continue
                if (masterBoard[x1][y1] == '@'):
                    print("You already placed a ship here. Try again.")
                    continue
            except ValueError:
                print("Wrong format try again.")
                continue
            break
        print("Your ship at", x1, y1, "was added to the map")
        masterBoard[x1][y1] = '@'

    printBoard()

def computerShips():
    global masterBoard
    i = 0
    while (i < 5):
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        if (masterBoard[x][y] == '@' or masterBoard[x][y] == '#'):
            continue
        else:
            masterBoard[x][y] = '#'
            print("Computer ship was added to board.")
        i += 1

    printBoard()

def playGame():
    hasComputerWon = False
    hasUserWon = False
    computerScore = 0
    userScore = 0
    while (computerScore < 5 and userScore < 5):
        print("Computer's score:", computerScore)
        print("Your score:", userScore)
        while True:
            try:
                print("Enter your guess between 0-9 with a space in between")
                x1, y1 = [int(i) for i in input().split()]
                print(x1, y1)
                if (x1 < 0 or x1 > 10):
                    print("Invalid X coordinate. Must be 0-9.")
                    continue
                if (y1 < 0 or y1 > 10):
                    print("Invalid Y coordinate. Must be 0-9.")
                    continue
                if (masterBoard[x1][y1] == '-' or masterBoard[x1][y1] == 'x'):
                    print("This spot was already guessed. Try again.")
                    continue
            except ValueError:
                print("Wrong format try again.")
                continue
            break
        if (masterBoard[x1][y1] == '@'):
            print("Oh no! You hit one of your own ships.")
            computerScore += 1
            masterBoard[x1][y1] = 'x'
        elif (masterBoard[x1][y1] == '#'):
            print("BOOM! You hit a computer ship!")
            userScore += 1
            masterBoard[x1][y1] = 'x'
        else:
            print("You missed. Now it's the computer's turn.")
            masterBoard[x1][y1] = '-'
        printBoard()
        if (userScore == 5):
            hasUserWon = True
            break
        
        while True:
            c1 = random.randint(0, 9)
            c2 = random.randint(0, 9)
            if (masterBoard[c1][c2] == 'x' or masterBoard[c1][c2] == '-'):
                continue
            break

        if (masterBoard[c1][c2] == '@'):
            print("Oh no! The computer sunk one of your ships!")
            computerScore += 1
            masterBoard[c1][c2] = 'x'
        elif (masterBoard[c1][c2] == '#'):
            print("The computer sunk one of their own ships!")
            userScore += 1
            masterBoard[c1][c2] = 'x'
        else:
            print("The computer missed. Now it's your turn.")
            masterBoard[c1][c2] = '-'
        
        printBoard()
        if (computerScore == 5):
            hasComputerWon = True

    if (hasComputerWon):
        print("The Computer won. Better luck next time!")
    else:
        print("Congrats, you won!")
            
    
        
main()
