# 12

def is_identity_matrix():
    matrix = []
    print("Enter the elements of the 3x3 matrix row by row:")
    for i in range(3):
        row = list(map(int, input("Enter row " + str(i + 1) + ": ").split()))
        matrix.append(row)

    for i in range(3):
        for j in range(3):
            if i == j and matrix[i][j] != 1:
                print("False")
                return
            elif i != j and matrix[i][j] != 0:
                print("False")
                return
    print("True")

is_identity_matrix()