
def print_board(board):
    for i in range(len(board)):
        if i%3 == 0:
            print("-------------------------")
        rowPrint = ""
        for j in range(len(board[0])):
        
            if board[i][j] != 0:
                if j%3 == 0:
                    rowPrint +=  "| " + str(board[i][j])+ " "
                else:
                    if j == 8:
                        rowPrint +=  str(board[i][j])+ " |"
                    else:
                        rowPrint +=   str(board[i][j])+ " "
            
            else:
                if j%3 == 0:
                    rowPrint +=  "|   "
                else:
                    if j == 8:
                        rowPrint +=  "  |"
                    else:
                        rowPrint +=  "  "
        print(rowPrint)
        
    print("-------------------------")


def find_zero (board):
    num_row = len(board)
    num_col = len(board[0])
    for i in range(num_row):
        for j in range(num_col):
            if board[i][j] == 0:
                zeroPos = [i,j]
                return zeroPos
    return None

def is_valid (board, row, col, value):
    if board[row].count(value) > 0:
        return 0
    for i in range(len(board)):
        if board[i][col] == value:
            return False
    startRow = (row //3)*3
    startCol = (col //3)*3

    for i in range (3):
        for j in range (3):
            if board[startRow + i][startCol + j] == value:
                return False
    return True

def solve (board):
    if find_zero(board) == None:
        return board
    else:
        zero_row = find_zero(board)[0]
        zero_col = find_zero(board)[1]
        for i in range (1,10):
            if is_valid(board, zero_row, zero_col, i):
                board[zero_row][zero_col] = i
                if solve(board) == None:
                    board[zero_row][zero_col] = 0
    
    if find_zero(board) == None:    
        return board 
    
    return None

board = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]

print ("Original unsorted")
print_board (board)
solution = solve(board)
print ("\nSolution")
print_board(solution)


