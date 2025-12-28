def matrix_multiplication(A, B):
    AB_rows = len(A)
    AB_cols = len(B[0])

    AB = []
    for y in range(AB_rows):
        row = []
        for x in range(AB_cols):
            row.append(0)
        AB.append(row)

    for i in range(AB_rows):
        for j in range(AB_cols):
            for k in range(len(B)):
                AB[i][j] += A[i][k] * B[k][j]

    return AB

def trace(A):
    diag_sum = 0

    for i in range(len(A)):
        diag_sum += A[i][i]
    
    return diag_sum

def main():
    Aa = [[0, 1, 1, 0, 0, 0],
         [1, 0, 1, 1, 1, 0],
         [1, 1, 0, 0, 1, 1],
         [0, 1, 0, 0, 1, 0],
         [0, 1, 1, 1, 0, 1],
         [0, 0, 1, 0, 1, 0]]
    

    Ab = [[0, 1, 1, 0, 0],
         [1, 0, 1, 1, 0],
         [1, 1, 0, 0, 1],
         [0, 1, 0, 0, 1],
         [0, 0, 1, 1, 0]]
    
    Ac = [[0, 1, 1, 1, 1],
         [1, 0, 1, 1, 1],
         [1, 1, 0, 1, 1],
         [1, 1, 1, 0, 1],
         [1, 1, 1, 1, 0]]
    
    matrices = [("Aa", Aa), ("Ab", Ab), ("Ac", Ac)]
    for name, matrix in matrices:
        print(f"Number of three-edge triangles in ({name}:", int(trace(matrix_multiplication(matrix_multiplication(matrix, matrix), matrix)) / 6))

main()
