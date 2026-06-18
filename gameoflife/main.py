import random

def random_state(width, height):
    board = []
    for y in range(height):
        row = []
        for x in range(width):
            var = random.random()
            if (var < 0.5):
                row.append(0)
            else:
                row.append(1)
        board.append(row)
    return board


width = 8
height = 8

def render(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end=" ")
        print("\n") 

# render(random_state(width, height))

def next_board_state(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (board[i][j] == 1):
                ## Only 0 or 1 live neighbours
                if (board[i-1][j] == 0 or board[i-1][j-1] == 0 or board[i][j-1] == 0 or board[i+1][j-1] == 0
                    or board[i+1][j] == 0 or board[i+1][j+1] == 0 or board[i][j+1] == 0 or board[i-1][j+1] == 0):
                    board[i][j] == 0
                
                ## 2 or 3 live neighbours
                ##TODO
                ct = 0
                if (board[i-1][j] == 1): 
                    ct = ct + 1
                if (board[i-1][j-1] == 1): 
                    ct = ct + 1
                if (board[i][j-1] == 1): 
                    ct = ct + 1
                if (board[i+1][j-1] == 1): 
                    ct = ct + 1
                if (board[i+1][j] == 1): 
                    ct = ct + 1
                if (board[i+1][j+1] == 1): 
                    ct = ct + 1
                if (board[i][j+1] == 1): 
                    ct = ct + 1
                if (board[i-1][j+1] == 1): 
                    ct = ct + 1
                
                if (ct >= 2 and ct <= 3):
                    board[i][j] = 1
                elif (ct > 3):
                    board[i][j] = 0
                
            else:
                ##TODO
                ct = 0
                if (board[i-1][j] == 1): 
                    ct = ct + 1
                if (board[i-1][j-1] == 1): 
                    ct = ct + 1
                if (board[i][j-1] == 1): 
                    ct = ct + 1
                if (board[i+1][j-1] == 1): 
                    ct = ct + 1
                if (board[i+1][j] == 1): 
                    ct = ct + 1
                if (board[i+1][j+1] == 1): 
                    ct = ct + 1
                if (board[i][j+1] == 1): 
                    ct = ct + 1
                if (board[i-1][j+1] == 1): 
                    ct = ct + 1
                

                if (ct == 3):
                    board[i][j] = 1
    return board

board1 = next_board_state(random_state(width, height))
render(board1)
            