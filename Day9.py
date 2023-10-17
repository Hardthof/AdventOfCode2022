import numpy as np

class move:
    def __init__(self, d, v):
        self.d = d
        self.v = v

class Grid:
    def __init__(self):
        self.x = int(0)
        self.y = int(0)
        self.s = (0,0)
        self.moves = []

coord_changes = {'L': lambda c: (c[0], c[1]-1), 
                 'R': lambda c: (c[0], c[1]+1), 
                 'U': lambda c: (c[0]+1, c[1]), 
                 'D': lambda c: (c[0]-1, c[1])}

def estimate_grid_size(seq):
    grid = Grid()
    max_x, max_y, min_x, min_y = 0,0,0,0
    x,y = 1,1
    for l in seq:
        d, v = l.split(' ')
        v = int(v)
        grid.moves.append(move(d,v))
        print(d, v)
        if d == 'D':
            x -= v
            min_x = min(min_x, x)
        elif d == 'U':
            x += v
            max_x = max(max_x, x)
        elif d == 'R':
            y += v
            max_y = max(max_y, y)
        elif d == 'L':
            y -= v
            min_y = min(min_y, y)
        else :
            RuntimeError('unkown direction')

    if min_x < 0 or min_y < 0:
        print(max_x, max_y, min_x, min_y)           
        max_x = max_x - min_x
        max_y = max_y - min_y
        grid.s = (-min_x, -min_y)
    grid.x = max_x
    grid.y = max_y
    return grid

def follow(visited_matrix, T, H, update = True):
    row1, col1 = T
    row2, col2 = H

    # neighbors no movement required 
    row_diff = abs(row1 - row2)
    col_diff = abs(col1 - col2)
    if row_diff <= 1 and col_diff <= 1:
        if update: visited_matrix[T] = '#'
        return T
    
    # linear movement
    if row1 == row2 or col1 == col2:
        average_row = (row1 + row2) // 2
        average_col = (col1 + col2) // 2
        if update: visited_matrix[average_row, average_col] = '#'
        return (average_row, average_col)
    
    # direction change
    # move row and col 1 in direction Head
    new_b = [T[0], T[1]]
    if H[0] < T[0]:
        new_b[0] -= 1
    elif H[0] > T[0]:
        new_b[0] += 1

    if H[1] < T[1]:
        new_b[1] -= 1
    elif H[1] > T[1]:
        new_b[1] += 1
    if update: visited_matrix[new_b[0], new_b[1]] = '#'
    return tuple(new_b) 

def printMatrix(grid, s, T, H):
    char_matrix = np.full((grid.x, grid.y), '.', dtype=str)
    char_matrix[s] = 's'
    char_matrix[T] = 'T'
    char_matrix[H] = 'H'
    print(char_matrix[::-1])

def printMatrix2(grid, s, tail, H):
    char_matrix = np.full((grid.x, grid.y), '.', dtype=str)
    char_matrix[s] = 's'
    for t in tail:
        char_matrix[tail[t]] = t
    char_matrix[H] = 'H'
    print(char_matrix[::-1])

def moveHead(visited_matrix, T, H, direction):
    H = coord_changes[direction](H)
    T = follow(visited_matrix, T,H)
    return T,H

def moveHeadAndTail(visited_matrix, tail, H, direction):
    H = coord_changes[direction](H)
    head = H
    for t in tail:       
        tail[t] = follow(visited_matrix, tail[t], head, t == 9)
        head = tail[t]
    return tail,H

if __name__ == '__main__':

    f = open('Day9.txt', mode='r')
    seq = [line.strip() for line in f]
    grid = estimate_grid_size(seq)
    char_matrix = np.full((grid.x,grid.y), '.', dtype=str)
    visited_matrix = np.copy(char_matrix)
    visited_matrix2 = np.copy(char_matrix)
    s = grid.s
    tail = {k: grid.s for k in range(1,10)}
    T = grid.s
    H = grid.s
    # printMatrix(grid, s, T, H)

    for order in grid.moves:
        for _ in range(order.v):
            #T,H = moveHead(visited_matrix, T, H, order.d)
            tail,H = moveHeadAndTail(visited_matrix2, tail, H, order.d)
            printMatrix2(grid, s, tail, H)
    # printMatrix(grid, s, T, H)
    print(visited_matrix2[::-1])
    print(np.count_nonzero(visited_matrix == '#'))
    print(np.count_nonzero(visited_matrix2 == '#'))