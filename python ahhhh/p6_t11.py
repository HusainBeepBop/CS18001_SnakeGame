# 11

def print_matrix():
    matrix = []
    print("Enter the elements of the 3x3 matrix row by row:")
    for i in range(3):
        row = list(map(int, input("Enter row " + str(i + 1) + ": ").split()))
        matrix.append(row)

    print("Row-wise elements:")
    for row in matrix:
        print(row)

    print("Column-wise elements:")
    for j in range(3):
        for i in range(3):
            print(matrix[i][j], end=" ")
        print()

print_matrix()