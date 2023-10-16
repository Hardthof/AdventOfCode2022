import numpy as np      

if __name__ == '__main__':
    
    matrix = []
    with open('Day8.txt', 'r') as file:
        for line in file:
            row = list(line.strip())
            matrix.append(row)

    matrix = np.array(matrix, dtype=int)
    bool_matrix = np.ones_like(matrix, dtype=bool)
    bool_matrix[1:-1,1:-1] = False

    for row_index in range(1, matrix.shape[0]-1):
        lMax = matrix[row_index, 0]
        rMax = matrix[row_index, -1]
        for i in range(1, matrix.shape[1] -1):
            if matrix[row_index, i] > lMax: 
                bool_matrix[row_index, i] = True
                lMax = matrix[row_index, i]
            if matrix[row_index, -(i+1)] > rMax: 
                bool_matrix[row_index, -(i+1)] = True
                rMax = matrix[row_index, -(i+1)]

    for col_index in range(1, matrix.shape[1]-1):
        tMax = matrix[0, col_index]
        bMax = matrix[-1, col_index]
        for i in range(1, matrix.shape[1] -1):
            if matrix[i, col_index] > tMax: 
                bool_matrix[i, col_index] = True
                tMax = matrix[i, col_index]
            if matrix[-(i+1), col_index] > bMax: 
                bool_matrix[-(i+1), col_index] = True
                bMax = matrix[-(i+1), col_index]

    view_score = np.zeros_like(matrix, dtype=int)
    
    best_score = 0
    for row_index in range(1, matrix.shape[0]-1):
        for col_index in range(1, matrix.shape[1]-1):
            element = matrix[row_index, col_index]
            l,r,t,b = 0,0,0,0

            for i in range(col_index -1, 0 -1, -1):
                l = l+1
                if element <= matrix[row_index, i]:
                    break

            for i in range(col_index + 1, matrix.shape[1]):
                r = r+1
                if element <= matrix[row_index, i]:
                    break

            for i in range(row_index -1, 0 -1, -1):
                t = t+1
                if element <= matrix[i, col_index]:
                    break

            for i in range(row_index + 1, matrix.shape[0]):
                b = b+1
                if element <= matrix[i, col_index]:
                    break

            score = l*r*t*b       
            if score > best_score:
                best_score = score

    print('best_score', best_score) 
