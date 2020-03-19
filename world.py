ROWS = 16
COLS = 16

board = [[False for x in range(ROWS)] for y in range(COLS)]
copy = [[False for x in range(ROWS)] for y in range(COLS)]


def calculateNextBoard():
    for x, row in enumerate(board):
        for y, elem in enumerate(row):
            copy[x][y] = nextState(x, y)

    for x, row in enumerate(board):
        for y, elem in enumerate(row):
            board[x][y] = copy[x][y]


def nextState(x, y):
    neighbors = getNeighbors(x, y)
    tile = board[x][y]
    if tile:

        if neighbors < 2:
            return False

        if 2 <= neighbors <= 3:
            return True

        if neighbors > 3:
            return False
    else:
        if neighbors == 3:
            return True


def getNeighbors(x, y):
    count = 0
    # general case
    if 0 < x < ROWS - 1 and 0 < y < COLS - 1:
        if board[x - 1][y - 1]:
            count += 1
        if board[x - 1][y]:
            count += 1
        if board[x - 1][y + 1]:
            count += 1
        if board[x][y - 1]:
            count += 1
        if board[x][y + 1]:
            count += 1
        if board[x + 1][y - 1]:
            count += 1
        if board[x + 1][y]:
            count += 1
        if board[x + 1][y + 1]:
            count += 1

    # top edge case
    elif x == 0 and 0 < y < COLS - 1:
        if board[ROWS - 1][y - 1]:
            count += 1
        if board[ROWS - 1][y]:
            count += 1
        if board[ROWS - 1][y + 1]:
            count += 1
        if board[x][y - 1]:
            count += 1
        if board[x][y + 1]:
            count += 1
        if board[x + 1][y - 1]:
            count += 1
        if board[x + 1][y]:
            count += 1
        if board[x + 1][y + 1]:
            count += 1

    # bottom edge case
    elif x == ROWS - 1 and 0 < y < COLS - 1:
        if board[x - 1][y - 1]:
            count += 1
        if board[x - 1][y]:
            count += 1
        if board[x - 1][y + 1]:
            count += 1
        if board[x][y - 1]:
            count += 1
        if board[x][y + 1]:
            count += 1
        if board[0][y - 1]:
            count += 1
        if board[0][y]:
            count += 1
        if board[0][y + 1]:
            count += 1

    # left edge case
    elif 0 < x < ROWS - 1 and y == 0:
        if board[x - 1][COLS - 1]:
            count += 1
        if board[x - 1][y]:
            count += 1
        if board[x - 1][y + 1]:
            count += 1
        if board[x][COLS - 1]:
            count += 1
        if board[x][y + 1]:
            count += 1
        if board[x + 1][COLS - 1]:
            count += 1
        if board[x + 1][y]:
            count += 1
        if board[x + 1][y + 1]:
            count += 1

    # right edge case
    elif 0 < x < ROWS - 1 and y == COLS - 1:
        if board[x - 1][y - 1]:
            count += 1
        if board[x - 1][y]:
            count += 1
        if board[x - 1][0]:
            count += 1
        if board[x][y - 1]:
            count += 1
        if board[x][0]:
            count += 1
        if board[x + 1][y - 1]:
            count += 1
        if board[x + 1][y]:
            count += 1
        if board[x + 1][0]:
            count += 1

    # top-left corner case
    elif x == 0 and y == 0:
        if board[ROWS - 1][y]:
            count += 1
        if board[ROWS - 1][y + 1]:
            count += 1
        if board[ROWS - 1][COLS - 1]:
            count += 1
        if board[x][y + 1]:
            count += 1
        if board[x + 1][y]:
            count += 1
        if board[x + 1][y + 1]:
            count += 1
        if board[x][COLS - 1]:
            count += 1
        if board[x + 1][COLS - 1]:
            count += 1

    # bottom-left corner case
    elif x == ROWS - 1 and y == 0:
        if board[0][y]:
            count += 1
        if board[0][y + 1]:
            count += 1
        if board[0][COLS - 1]:
            count += 1
        if board[x - 1][y]:
            count += 1
        if board[x - 1][y + 1]:
            count += 1
        if board[x - 1][COLS - 1]:
            count += 1
        if board[x][y + 1]:
            count += 1
        if board[x][COLS - 1]:
            count += 1

    # top-right corner case
    elif x == 0 and y == COLS - 1:
        if board[x][0]:
            count += 1
        if board[x][y - 1]:
            count += 1
        if board[x + 1][0]:
            count += 1
        if board[x + 1][y - 1]:
            count += 1
        if board[x + 1][y]:
            count += 1
        if board[ROWS - 1][0]:
            count += 1
        if board[ROWS - 1][y - 1]:
            count += 1
        if board[ROWS - 1][y]:
            count += 1

    # bottom right corner case
    elif x == ROWS - 1 and y == COLS - 1:
        if board[x][0]:
            count += 1
        if board[x][y - 1]:
            count += 1
        if board[x - 1][0]:
            count += 1
        if board[x - 1][y - 1]:
            count += 1
        if board[x - 1][y]:
            count += 1
        if board[0][0]:
            count += 1
        if board[0][y - 1]:
            count += 1
        if board[0][y]:
            count += 1

    return count


def printBoard():
    for row in board:
        for index, elem in enumerate(row):
            if index % ROWS == 0:
                print("")
            if not elem:
                print("*", end=" ")
            else:
                print("O", end=" ")
    print()
def choosePreset(preset):
    if preset == "Glider":
        board[11][9] = True
        board[11][10] = True
        board[11][11] = True
        board[10][11] = True
        board[9][10] = True
    elif preset == "Pulsar":
        board[1][3] = True
        board[1][4] = True
        board[1][5] = True
        board[1][9] = True
        board[1][10] = True
        board[1][11] = True

        board[3][1] = True
        board[3][6] = True
        board[3][8] = True
        board[3][13] = True

        board[4][1] = True
        board[4][6] = True
        board[4][8] = True
        board[4][13] = True

        board[5][1] = True
        board[5][6] = True
        board[5][8] = True
        board[5][13] = True

        board[6][3] = True
        board[6][4] = True
        board[6][5] = True
        board[6][9] = True
        board[6][10] = True
        board[6][11] = True

        board[8][3] = True
        board[8][4] = True
        board[8][5] = True
        board[8][9] = True
        board[8][10] = True
        board[8][11] = True

        board[9][1] = True
        board[9][6] = True
        board[9][8] = True
        board[9][13] = True

        board[10][1] = True
        board[10][6] = True
        board[10][8] = True
        board[10][13] = True

        board[11][1] = True
        board[11][6] = True
        board[11][8] = True
        board[11][13] = True

        board[13][3] = True
        board[13][4] = True
        board[13][5] = True
        board[13][9] = True
        board[13][10] = True
        board[13][11] = True

    elif preset == "Spaceship":
        board[9][9] = True
        board[9][10] = True

        board[10][8] = True
        board[10][9] = True
        board[10][10] = True
        board[10][11] = True

        board[11][8] = True
        board[11][9] = True
        board[11][11] = True
        board[11][12] = True

        board[12][10] = True
        board[12][11] = True


print("Choose a Preset:\nGlider\nPulsar\nSpaceship\n");
chosenPreset = input()
choosePreset(chosenPreset)
printBoard()
print("Advance? (Y/N)")
advance = input()
while advance == "Y":
    calculateNextBoard()
    printBoard()
    print("Advance? (Y/N)")
    advance = input()
