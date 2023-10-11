def transpose_matrix(matrix):
    size = len(matrix)
    for i in range(size):
        for j in range(i+1, size):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


size = int(input())
matrix = [[i+1 for i in range(size)] for j in range(size)]
for row in matrix:
    print(", ".join(map(str, row)))
transpose_matrix(matrix)
for row in matrix:
    print(", ".join(map(str, row)))
