# Pluck and plant game
import random
import time
# This is a one player game in which the user must find a flower on the
# game board. The user has their own character that they can see on the board.
# This is the character they will move to pick up the flower, which is represented
# by another special character on the game board. Once the user has picked up the flower
# they will need to find the target spot to drop off the flower. Once the user
# has dropped off the flower at the target spot, then they've won the game.

def main():
    # masterBoard is the 2d array we will use and change throughout the program
    # to represent the game board. 
    global masterBoard
    again = True
    while (again):
        rows = 5
        columns = 5
        masterBoard = constructBoard(rows, columns)
        print("""Welcome to pluck and plant game. You will play as a kangaroo and
        try to return a flower to the return position in the gardenn.""")   
        kangarooPosition = []
        endPosition = []
        printGarden()
        kangarooPosition = assignPositions()
        endPosition = findFlower(kangarooPosition)
        again = findTarget(endPosition)
        
    print("Goodbye!")
    time.sleep(5)
    

# This function will construct the game board for us using row and column
# integer values passed into the function. 
def constructBoard(rows, columns):
    createBoard = [['0' for i in range(rows)] for j in range(columns)]
    return createBoard

# This function will print out the current state of the game board to the console.
# printGarden() will be needed in multiple functions so that the user is aware of
# where they are located on the map, and where they need to get to to win the game. 
def printGarden():
    global masterBoard
    print()
    print("$ is the return position and * is the flower you need to get")
    print("GARDEN")
    print("  01234")
    for i in range(len(masterBoard)):
        line = "" + str(i) + "|"
        for j in range(len(masterBoard[i])):
            line += str(masterBoard[i][j])
        print(line + "|" + str(i))

    print("  01234")
    print()

# Assign the positions of the special characters on the game board.
# Note that the character '$' represents the return position where the player needs
# return the flower to. The * character represents the flower that the player needs
# to move to first. 
def assignPositions():
    global masterBoard
    # Use two random integers for the flower position. 
    c1 = random.randint(0, 4)
    c2 = random.randint(0, 4)
    masterBoard[c1][c2] = '*'
    while True:
        # Use two random integers for the return position. 
        r1 = random.randint(0, 4)
        r2 = random.randint(0, 4)
        # Make sure that the flower and return position aren't in the same spot. 
        if (masterBoard[r1][r2] == '*'):
            continue
        else:
            break
    
    masterBoard[r1][r2] = '$'
    printGarden()
   
    print("""Enter below the coordinates of where you want to start. Seperate
    your input by using a space in between the 2 coordinates.""")

    # This while True and try block will validate the x and y coordinates of where
    # the user wants to place their character on the board. 
    while True:
        try:
            print("Enter two numbers between 0-4 with a space in between")
            x1, y1 = [int(i) for i in input().split()]
            print(x1, y1)
            if (x1 < 0 or x1 > 4):
                print("Invalid X coordinate. Must be 0-9.")
                continue
            if (y1 < 0 or y1 > 4):
                print("Invalid Y coordinate. Must be 0-9.")
                continue
            if (masterBoard[x1][y1] == '*' or masterBoard[x1][y1] == '$'):
                print("You can't move here. Try again.")
                continue
        # Display an alert to the console if the user didn't follow the instructions
        # and seperate their integers by a space, or didn't enter two integers at all. 
        except ValueError:
            print("Wrong format try again.")
            continue
        break
    
    startingPosition = [x1, y1]
    # Note that K will be the character which represents the user's current position. 
    masterBoard[x1][y1] = 'K'
    print("Your kangaroo position has been set in the garden")
    printGarden()
    return startingPosition

# Start is an array of two integers passed into the function which represent
# Both the x and y coordinates of where the K, or starting position of the user
# currently is on the board. 
def findFlower(start):
    global masterBoard
    print("Now we need to find and pick up the flower.")
    currentXLocation = start[0]
    currentYLocation = start[1]
    hasFound = False
    # This is the main game loop. 
    while (hasFound == False):
        userChoice = ""
        # Use a while true and try block to get the user's input on which direction
        # they want to move in. Make sure their choice is a valid letter consisting
        # of l for left, d for down, u for up, or r for right. 
        while True:
            try:
                userChoice = input("Enter l to move left, r to move right, d for Down, and u for up:")
                if (userChoice != 'l' and userChoice != 'r' and userChoice != 'u' and userChoice != 'd'):
                    print("Invalid choice. Try again.")
                    continue
            except ValueError:
                print("Incorrect format. Try again.")
                continue
            break
        
        if (userChoice == 'l'):
            cantMove = checkHitWall(currentYLocation, 'l')
            if (cantMove):
                print("You can't move left. Choose another option.")
                continue
            else:
                hitReturn = checkHitReturn(currentXLocation, currentYLocation, 'l')
                if (hitReturn):
                    print("You can't run over the return spot yet.")
                    continue
                
                # The move is valid, so change the current character that the user is at
                # to the default map character of '0', and move the character's
                # symbol K to the left by one.
                hasFound = checkFoundFlower(currentXLocation, currentYLocation - 1)
                if (hasFound):
                    print("Flower was found!")
                    changeChars(currentXLocation, currentYLocation, 'l')
                    currentYLocation -= 1
                    break
                else:
                    changeChars(currentXLocation, currentYLocation, 'l')
                    currentYLocation -= 1
                    
        elif (userChoice == 'r'):
            cantMove = checkHitWall(currentYLocation, 'r')
            if (cantMove):
                print("You can't move right. Choose another option.")
                continue
            else:
                hitReturn = checkHitReturn(currentXLocation, currentYLocation, 'r')
                if (hitReturn):
                    print("You can't run over the return spot yet.")
                    continue
                
                # The move is valid, so change the current character that the user is at
                # to the default map character of '0', and move the character's
                # symbol K to the right by one.

                hasFound = checkFoundFlower(currentXLocation, currentYLocation + 1)
                if (hasFound):
                    print("Flower was found!")
                    changeChars(currentXLocation, currentYLocation, 'r')
                    currentYLocation += 1
                    break
                else:
                    changeChars(currentXLocation, currentYLocation, 'r')
                    currentYLocation += 1
                
        elif (userChoice == 'd'):
            cantMove = checkHitWall(currentXLocation, 'd')
            if (cantMove):
                print("You can't move down. Choose another option.")
                continue
            else:
                hitReturn = checkHitReturn(currentXLocation, currentYLocation, 'd')
                if (hitReturn):
                    print("You can't run over the return spot yet.")
                    continue
                
                # The move is valid, so change the current character that the user is at
                # to the default map character of '0', and move the character's
                # symbol K to the down by one.
                hasFound = checkFoundFlower(currentXLocation + 1, currentYLocation)
                if (hasFound):
                    print("Flower was found!")
                    changeChars(currentXLocation, currentYLocation, 'd')
                    currentXLocation += 1
                    break
                else:
                    changeChars(currentXLocation, currentYLocation, 'd')
                    currentXLocation += 1
                    
        elif (userChoice == 'u'):
            cantMove = checkHitWall(currentXLocation, 'u')
            if (cantMove):
                print("You can't move up. Choose another option.")
                continue
            else:
                hitReturn = checkHitReturn(currentXLocation, currentYLocation, 'u')
                if (hitReturn):
                    print("You can't run over the return spot yet.")
                    continue
                
                # The move is valid, so change the current character that the user is at
                # to the default map character of '0', and move the character's
                # symbol K to the down by one.
                hasFound = checkFoundFlower(currentXLocation - 1, currentYLocation)
                if (hasFound):
                    print("Flower was found!")
                    changeChars(currentXLocation, currentYLocation, 'u')
                    currentXLocation -= 1
                    break
                else:
                    changeChars(currentXLocation, currentYLocation, 'u')
                    currentXLocation -= 1
        printGarden()           

    # rArray will retun an array of the current coordinates to main
    # so that the next function findTarget() will know where to start the
    # the user's character 'K'
    printGarden()            
    rArray = [currentXLocation, currentYLocation]
    return rArray

# Check to see if the user ran into a wall based on their current position
# and the direction they inputted. 
def checkHitWall(currentPos, direction):
    if (currentPos == 0 and direction == 'u') or (currentPos == 0 and direction == 'l') or (currentPos == 4 and direction == 'r') or (currentPos == 4 and direction == 'd'):
        return True
    else:
        return False

# Check to see if the user found the flower on the map. 
def checkFoundFlower(currentX, currentY):
    global masterBoard
    if (masterBoard[currentX][currentY] == '*'):
        return True
    else:
        return False

# Check to see if the user ran over the return position. 
def checkHitReturn(currentXPos, currentYPos, direction):
    global masterBoard
    if (direction == 'l'):
        if (masterBoard[currentXPos][currentYPos - 1] == '$'):
            return True
        else:
            return False
    elif (direction == 'r'):
        if (masterBoard[currentXPos][currentYPos + 1] == '$'):
            return True
        else:
            return False
    elif (direction == 'd'):
        if (masterBoard[currentXPos + 1][currentYPos] == '$'):
            return True
        else:
            return False
    else:
        if (masterBoard[currentXPos - 1][currentYPos] == '$'):
            return True
        else:
            return False
        
# This function will handle the character shift once the user finds the flower.
# We need the character on the map where the flower used to be to now
# display a 'K'. We also need the character where the user previously moved from
# to display an ordinary '0' character, which denotes that the space is now empty.
def changeChars(currentX, currentY, direction):
    global masterBoard
    if (direction == 'l'):
        masterBoard[currentX][currentY] = '0'
        masterBoard[currentX][currentY - 1] = 'K'
    elif (direction == 'r'):
        masterBoard[currentX][currentY] = '0'
        masterBoard[currentX][currentY + 1] = 'K'
    elif (direction == 'd'):
        masterBoard[currentX][currentY] = '0'
        masterBoard[currentX + 1][currentY] = 'K'
    else:
        masterBoard[currentX][currentY] = '0'
        masterBoard[currentX - 1][currentY] = 'K'

def foundReturn(x, y):
    global masterBoard
    if (masterBoard[x][y] == '$'):
        return True
    else: return False

# Second function which represents the main logic of the game. Once the user
# has found the flower, they need to move to the return position on the board
# marked as '$' where they will plant the flower and win the game. 
def findTarget(endArray):
    print("Now we need to plant the flower in the return spot in the garden to win the game.")
    currentX = endArray[0]
    currentY = endArray[1]
    hasFound = False
    while (hasFound == False):
        userChoice = ""
        while True:
            try:
                userChoice = input("Enter l to move left, r to move right, d for Down, and u for up:")
                if (userChoice != 'l' and userChoice != 'r' and userChoice != 'u' and userChoice != 'd'):
                    print("Invalid choice. Try again.")
                    continue
            except ValueError:
                print("Incorrect format. Try again.")
                continue
            break

        # We only need to check if the user is either trying to run into a wall
        # or if they have found the correct return spot since there is
        # no flower character on the board anymore. 
        if (userChoice == 'l'):
            # Check if the user is trying to run into a wall
            cantMove = checkHitWall(currentY, 'l')
            if (cantMove):
                print("You can't move left. Choose another option.")
                continue
            else:
                # foundReturn function will return true if the current X and
                # Y location correspond with the '$' return character on the
                # game board, and kill the while loop if the user did win.
                if (foundReturn(currentX, currentY - 1) == True):
                    print("Return spot found! Plant the flower now.")
                    hasFound = True
                masterBoard[currentX][currentY] = '0'
                currentY -= 1
                masterBoard[currentX][currentY] = 'K'

        elif (userChoice == 'r'):
            # Check if the user is trying to run into a wall
            cantMove = checkHitWall(currentY, 'r')
            if (cantMove):
                print("You can't move left. Choose another option.")
                continue
            else:
                # foundReturn function will return true if the current X and
                # Y location correspond with the '$' return character on the
                # game board, and kill the while loop if the user did win.
                if (foundReturn(currentX, currentY + 1) == True):
                    print("Return spot found! Plant the flower now.")
                    hasFound = True
                masterBoard[currentX][currentY] = '0'
                currentY += 1
                masterBoard[currentX][currentY] = 'K'
                
        elif (userChoice == 'd'):
            # Check if the user is trying to run into a wall
            cantMove = checkHitWall(currentX, 'd')
            if (cantMove):
                print("You can't move left. Choose another option.")
                continue
            else:
                # foundReturn function will return true if the current X and
                # Y location correspond with the '$' return character on the
                # game board, and kill the while loop if the user did win.
                if (foundReturn(currentX + 1, currentY) == True):
                    print("Return spot found! Plant the flower now.")
                    hasFound = True
                masterBoard[currentX][currentY] = '0'
                currentX += 1
                masterBoard[currentX][currentY] = 'K'
                
        elif (userChoice == 'u'):
            # Check if the user is trying to run into a wall
            cantMove = checkHitWall(currentX, 'u')
            if (cantMove):
                print("You can't move left. Choose another option.")
                continue
            else:
                # foundReturn function will return true if the current X and
                # Y location correspond with the '$' return character on the
                # game board, and kill the while loop if the user did win.
                if (foundReturn(currentX - 1, currentY) == True):
                    print("Return spot found! Plant the flower now.")
                    hasFound = True
                masterBoard[currentX][currentY] = '0'
                currentX -= 1
                masterBoard[currentX][currentY] = 'K'
                
        printGarden()

      ##    masterBoard[currentX][currentY] = '*'
##    if (currentY != 4):
##        masterBoard[currentX][currentY + 1] = 'K'
##    else:
##        masterBoard[currentX][currentY - 1] = 'K'
    # Use a boolean return value to determine whether or not the user wants
    # to play the game again.
    print("Congrats, you won!")
    again = input("Press y if you want to play again: ")
    if (again == 'y' or again == 'Y'):
        return True
    else:
        return False
    
main()

