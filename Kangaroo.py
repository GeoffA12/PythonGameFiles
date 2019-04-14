# Assignment 9 pluck and plant
import random
def main():
    global masterBoard
    m = 5
    n = 5
    masterBoard = [['0' for i in range(m)] for j in range(n)]
    print("""Welcome to pluck and plant game. You will play as a kangaroo and
    try to return a flower to the return position in the gardenn.""")   
    kangarooPosition = []
    endPosition = []
    printGarden()
    kangarooPosition = assignPositions()
    endPosition = findFlower(kangarooPosition)
    findTarget(endPosition)
    
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

def assignPositions():
    global masterBoard
    c1 = random.randint(0, 4)
    c2 = random.randint(0, 4)
    masterBoard[c1][c2] = '*'
    while True:
        r1 = random.randint(0, 4)
        r2 = random.randint(0, 4)
        if (masterBoard[r1][r2] == '*'):
            continue
        else:
            break
    print("Flower and return position have now been set.")
    masterBoard[r1][r2] = '$'
    printGarden()
   
    print("""Enter below the coordinates of where you want to start. Seperate
    your input by using a space in between the 2 coordinates.""")
    
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
        except ValueError:
            print("Wrong format try again.")
            continue
        break
    
    startingPosition = [x1, y1]
    masterBoard[x1][y1] = 'K'
    print("Your kangaroo position has been set in the garden")
    printGarden()
    return startingPosition

def findFlower(start):
    global masterBoard
    print("Now we need to find and pick up the flower.")
    kx = start[0]
    ky = start[1]
    print(kx, ky)
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
        if (userChoice == 'l'):
            if (ky == 0):
                print("You can't move left. Choose another option.")
                continue
            else:
                if (masterBoard[kx][ky - 1] == '$'):
                    print("You can't run over the return spot yet.")
                    continue
                masterBoard[kx][ky] = '0'
                ky -= 1
                
                if (masterBoard[kx][ky] == '*'):
                    print("Flower was found!")
                    hasFound = True
                masterBoard[kx][ky] = 'K'
        elif (userChoice == 'r'):
            if (ky == 4):
                print("You can't move right. Choose another option.")
                continue
            else:
                if (masterBoard[kx][ky + 1] == '$'):
                    print("You can't run over the return spot yet.")
                    continue
                masterBoard[kx][ky] = '0'
                ky += 1
                if (masterBoard[kx][ky] == '*'):
                    print("Flower was found!")
                    hasFound = True
                masterBoard[kx][ky] = 'K'
        elif (userChoice == 'd'):
            if (kx == 4):
                print("You can't move down. Try another option.")
                continue
            else:
                if (masterBoard[kx + 1][ky] == '$'):
                    print("You can't run over the return spot yet.")
                    continue
                masterBoard[kx][ky] = '0'
                kx += 1
                if (masterBoard[kx][ky] == '*'):
                    print("Flower was found!")
                    hasFound = True
                masterBoard[kx][ky] = 'K'
        elif (userChoice == 'u'):
            if(kx == 0):
                print("You can't move up. Try another option.")
                continue
            else:
                if (masterBoard[kx - 1][ky] == '$'):
                    print("You can't run over the return spot yet.")
                    continue
                masterBoard[kx][ky] = '0'
                kx -= 1
                if (masterBoard[kx][ky] == '*'):
                    print("Flower was found!")
                    hasFound = True
                masterBoard[kx][ky] = 'K'

        printGarden()
                
    rArray = [kx, ky]
    return rArray

def findTarget(endArray):
    print("Now we need to plant the flower in the return spot in the garden to win the game.")
    kx = endArray[0]
    ky = endArray[1]
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

        if (userChoice == 'l'):
            if (ky == 0):
                print("You can't move left. Choose another option.")
                continue
            else:
                if (masterBoard[kx][ky - 1] == '$'):
                    print("Return spot found! Plant the flower now.")
                    hasFound = True
                masterBoard[kx][ky] = '0'
                ky -= 1
                masterBoard[kx][ky] = 'K'
        elif (userChoice == 'r'):
            if (ky == 4):
                print("You can't move right. Choose another option.")
                continue
            else:
                if (masterBoard[kx][ky + 1] == '$'):
                    print("Return spot found! Plant the flower now.")
                    hasFound = True
                masterBoard[kx][ky] = '0'
                ky += 1
                masterBoard[kx][ky] = 'K'
        elif (userChoice == 'd'):
            if (kx == 4):
                print("You can't move down. Try another option.")
                continue
            else:
                if (masterBoard[kx + 1][ky] == '$'):
                    print("Return spot found! Plant the flower now.")
                    hasFound = True
                masterBoard[kx][ky] = '0'
                kx += 1
                masterBoard[kx][ky] = 'K'
        elif (userChoice == 'u'):
            if(kx == 0):
                print("You can't move up. Try another option.")
                continue
            else:
                if (masterBoard[kx - 1][ky] == '$'):
                    print("Return spot found! Plant the flower now.")
                    hasFound = True
                masterBoard[kx][ky] = '0'
                kx -= 1
                masterBoard[kx][ky] = 'K'
        printGarden()

    print("Congrats, you won!")
    masterBoard[kx][ky] = '*'
    if (ky != 4):
        masterBoard[kx][ky + 1] = 'K'
    else:
        masterBoard[kx][ky - 1] = 'K'
    printGarden()

main()
