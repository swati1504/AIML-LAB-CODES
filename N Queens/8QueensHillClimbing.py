import random
N = 8

def start(board,state):
    for i in range(0,N):
        num = random.randrange(0,N,1)
        state[i] = num
        board[state[i]][i] = 1

def printb(board):
    for i in range(0,N):
        print("\n")
        for j in range(0,N):
            print(board[i][j], end=" ")
            #print(" ")

def prints(state):
    for i in range(0,N):
        print(state[i])
        print(" ")

def compare(state1, state2):
    for i in range(0,N):
        if state1[i]!=state2[i]:
            return False
    return True

def fill(board, value):
    for i in range(0,N):
        for j in range(0,N):
            board[i][j] = value

def objective(board, state):
    attacking = 0
    row = 0
    col = 0
    for i in range(0, N):
        row = state[i] 
        col = i - 1
        while col >= 0 and board[row][col] != 1:
            col = col-1
        if col >= 0 and board[row][col] == 1:
            attacking = attacking+1

        row = state[i]
        col = i + 1
        while col < N and board[row][col] != 1:
            col = col+1
        if col < N and board[row][col] == 1:
            attacking = attacking+1

        row = state[i] - 1
        col = i - 1
        while col >= 0 and row >= 0 and board[row][col] != 1:
            col = col-1
            row = row -1
        if col >= 0 and row >= 0 and board[row][col] == 1:
            attacking = attacking+1
 
        row = state[i] + 1
        col = i + 1
        while col < N and row < N and board[row][col] != 1:
            col = col+1
            row = row+1
        if col < N and row < N and board[row][col] == 1:
            attacking = attacking+1
 
        row = state[i] + 1
        col = i - 1
        while col >= 0 and row < N and board[row][col] != 1:
            col = col-1
            row = row+1
        if col >= 0 and row < N and board[row][col] == 1:
            attacking = attacking+1
 
        row = state[i] - 1
        col = i + 1
        while col < N and row >= 0 and board[row][col] != 1:
            col = col+1
            row = row-1
        if col < N and row >= 0 and board[row][col] == 1:
            attacking = attacking+1
    return attacking//2

def generate(board, state):
    fill(board,0)
    for i in range(0,N):
        board[state[i]][i] = 1

def copystate(state1, state2):
    for i in range(0,N):
        state1[i] = state2[i]

def neighbour(board, state):
    state2 = [-1,-1,-1,-1,-1,-1,-1,-1]
    board2 = [[0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0]]
    copystate(state2, state)
    generate(board2, state2)

    objectiveB = objective(board2, state2)

    stateN = [-1,-1,-1,-1,-1,-1,-1,-1]
    boardN = [[0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0]]
    copystate(stateN, state)
    generate(boardN, stateN)

    for i in range(0,N):
        for j in range(0,N):
            if j!=state[i]:
                stateN[i] = j
                boardN[stateN[i]][i] = 1
                boardN[state[i]][i] = 0
                temp = objective(boardN, stateN)
                if temp<=objectiveB:
                    objectiveB = temp
                    copystate(state2, stateN)
                    generate(board2, state2)
                boardN[stateN[i]][i] = 0
                stateN[i] = state[i]
                boardN[state[i]][i] = 1
    copystate(state, state2)
    fill(board, 0)
    generate(board, state)

def hillClimb(board, state):
    stateN = [-1,-1,-1,-1,-1,-1,-1,-1]
    boardN = [[0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0]]
    copystate(stateN, state)
    generate(boardN, stateN)
    while True:
        copystate(state, stateN)
        generate(board, state)
        neighbour(boardN, stateN)
        if compare(state, stateN):
            printb(board)
            print(state)
            break
        elif objective(board, state)==objective(boardN, stateN):
            stateN[random.randrange(0,N,1)] = random.randrange(0,N,1)
            generate(boardN, stateN)     



if __name__ == '__main__':
    state = [-1,-1,-1,-1,-1,-1,-1,-1]
    board = [[0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0]]
    start(board,state)
    hillClimb(board, state)
