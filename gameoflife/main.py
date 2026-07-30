import random
import time
import os

ALIVE = '#'
DEAD = ' '

def load_board(filename, width, height):
    board = [[DEAD] * width for _ in range(height)]
    
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    for i, line in enumerate(lines):
        if i >= height:
            break
        line = line.rstrip('\n')  
        for j, char in enumerate(line):
            if j >= width:
                break
            board[i][j] = ALIVE if char == '#' else DEAD
    
    return board


def random_state(width, height):
    board = []
    for y in range(height):
        row = []
        for x in range(width):
            row.append(ALIVE if random.random() < 0.5 else DEAD)
        board.append(row)
    return board


def render(board):
    os.system('cls' if os.name == 'nt' else 'clear')  
    for row in board:
        print(''.join(row))  


def next_board_state(board):
    rows = len(board)
    cols = len(board[0])

    def ct_live_neighbours(r, c):
        ct = 0
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    ct += 1 if board[nr][nc] == ALIVE else 0
        return ct

    new_board = [[DEAD] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            neighbours = ct_live_neighbours(i, j)
            if board[i][j] == ALIVE:
                new_board[i][j] = ALIVE if neighbours in (2, 3) else DEAD
            else:
                new_board[i][j] = ALIVE if neighbours == 3 else DEAD

    return new_board


def run_forever(init_state):
    next_state = init_state
    while True:
        render(next_state)
        next_state = next_board_state(next_state)
        time.sleep(0.1)  


init_state = load_board('gun.txt', 25, 38)
run_forever(init_state)