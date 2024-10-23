def create_matrix():
    rows=int(input("Enter Number of rows: \n"))
    column=int(input("Enter Number of columns: \n"))
    matrix = []
    for i in range(rows):
        row = []
        for j in range(column):
            value = int(input(f"Enter value for matrix[{i}][{j}]: "))
            row.append(value)
        matrix.append(row)
    return matrix

def display_matrix(matrix):
    print("The Matrix is: ")
    for row in matrix:
        print("\t".join(map(str, row)))

def get_matrix_dimensions(matrix):
    if not matrix:  
        return 0, 0
    rows = len(matrix)
    cols = len(matrix[0])
    return rows, cols

def matrix_add():
    print("First Matrix: ")
    Matrix_1 = create_matrix()
    row1,col1 = get_matrix_dimensions(Matrix_1)
    print("Second Matrix: ")
    Matrix_2=create_matrix()
    row2,col2=get_matrix_dimensions(Matrix_2)
    if(row1!=row2 and col1!=col2):
        print("INVALID ARGUMENTS\n")
    else:
         result = [[0 for _ in range(col1)] for _ in range(row1)]
    
    for i in range(row1):
        for j in range(col1):
            result[i][j] = Matrix_1[i][j] + Matrix_2[i][j]
    
    return result

def matrix_sub():
    print("First Matrix: ")
    Matrix_1 = create_matrix()
    row1,col1 = get_matrix_dimensions(Matrix_1)
    print("Second Matrix: ")
    Matrix_2=create_matrix()
    row2,col2=get_matrix_dimensions(Matrix_2)
    if row1 != row2 and col1 != col2:
        print("INVALID ARGUMENTS\n")
    else:
         result = [[0 for _ in range(col1)] for _ in range(row1)]
    
    for i in range(row1):
        for j in range(col1):
            result[i][j] = Matrix_1[i][j] - Matrix_2[i][j]
    
    return result

def matrix_multiply():
    print("First Matrix: ")
    matrix1 = create_matrix()
    print("Second Matrix: ")
    matrix2=create_matrix()
    rows_matrix1 = len(matrix1)
    cols_matrix1 = len(matrix1[0])
    rows_matrix2 = len(matrix2)
    cols_matrix2 = len(matrix2[0])

    if cols_matrix1 != rows_matrix2:
        raise ValueError("Matrices cannot be multiplied")

    # Initialize the result matrix with zeros
    result = [[0 for _ in range(cols_matrix2)] for _ in range(rows_matrix1)]

    # Perform multiplication
    for i in range(rows_matrix1):
        for j in range(cols_matrix2):
            for k in range(cols_matrix1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result

def scalar_multiply():
    print("Enter Matrix Details: ")
    matrix=create_matrix()
    scalar=int(input("Input Scalar Value: "))
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Initialize the result matrix with zeros
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix[i][j] * scalar
    
    return result

def transpose_matrix(
    ):
    matrix=create_matrix()
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Initialize the result matrix with zeros
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]
    
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
    
    return transposed

def determinant(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    if rows!=cols:
        print("Determinant cannot be found for rectangular matrix!")
    else:
        if len(matrix) == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        else:
            det = 0
            for c in range(len(matrix)):
                det += ((-1) ** c) * matrix[0][c] * determinant(get_submatrix(matrix, 0, c))


        return det
    
def minor(matrix, row, col):
    submatrix = get_submatrix(matrix, row, col)
    return determinant(submatrix)

def get_submatrix(matrix, row, col):
    return [row[:col] + row[col+1:] for row in (matrix[:row] + matrix[row+1:])]

def get_matrix_minor(matrix, i, j):
    return [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]

def get_matrix_determinant(matrix):
    # Base case for 2x2 matrix
    
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    determinant = 0
    for c in range(len(matrix)):
        determinant += ((-1) ** c) * matrix[0][c] * get_matrix_determinant(get_matrix_minor(matrix, 0, c))
    return determinant

def get_matrix_inverse(matrix):
    determinant = get_matrix_determinant(matrix)
    if determinant == 0:
        raise ValueError("Matrix is singular and cannot be inverted.")

    # Special case for 2x2 matrix:
    if len(matrix) == 2:
        return [[matrix[1][1] / determinant, -1 * matrix[0][1] / determinant],
                [-1 * matrix[1][0] / determinant, matrix[0][0] / determinant]]

    # Find matrix of cofactors
    cofactors = []
    for r in range(len(matrix)):
        cofactorRow = []
        for c in range(len(matrix)):
            minor = get_matrix_minor(matrix, r, c)
            cofactorRow.append(((-1) ** (r + c)) * get_matrix_determinant(minor))
        cofactors.append(cofactorRow)
    cofactors = list(map(list, zip(*cofactors)))  # Transpose the matrix

    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c] / determinant
    return cofactors

def scalar_division():
    print("Enter Matrix Details: ")
    matrix=create_matrix()
    scalar=int(input("Input Scalar Value: "))
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Initialize the result matrix with zeros
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix[i][j] / scalar
    
    return result

def menu():
    print("\nMATRIX OPERATIONS\n\n")
    print("\nMenu:")
    print("1. Matrix Addition")
    print("2. Matrix Subtraction")
    print("3. Matrix Multiplication")
    print("4. Scalar Matrix Multiplication")
    print("5. Transpose of a Matrix")
    print("6. Minor of a Matrix")
    print("7. Determinant of a Matrix")
    print("8. Inverse of a Matrix")
    print("9. Matrix Scalar Division")
    print("0. Exit")

def main():
    while True:
        menu()
        choice = input("Enter your choice (0 - 9) : ")
        
        if choice == '0':
            print("Exiting the program.")
            break
        if choice in ['1', '2', '3', '4','5','6','7','8','9']:
            if choice == '1':
                print("Matrix Addition : \n")
                display_matrix(matrix_add())
            elif choice == '2':
                print("Matrix Subtraction : \n")
                display_matrix(matrix_sub())
            elif choice == '3':
                print("Matrix Multiplication : \n")
                display_matrix(matrix_multiply())
            elif choice == '4':
                print("Scalar Multiplication : \n")
                display_matrix(scalar_multiply())
            elif choice == '5':
                print("Transpose of The Matrix is : \n")
                display_matrix(transpose_matrix())
            elif choice == '6':
                matrix=create_matrix()
                row=int(input("Row of the element: "))
                column=int(input("Column of the element "))
                print("Minor of the Element : ",
                      minor(matrix,row,column))
            elif choice == '7':
                matrix=create_matrix()
                print("Determinant of the Matrix : ",determinant(matrix))
            elif choice == '8':
                matrix=create_matrix()
                try:
                        inverse = get_matrix_inverse(matrix)
                        print("Inverse of the matrix:")
                        for row in inverse:
                                print(row)
                except ValueError as e:
                        print(e)
            elif choice == '9':
                print("Scalar Division of the Matrix is: \n")
                display_matrix(scalar_division())

        else:
            print("Invalid choice, please enter a number between 1 and 9.")

main()
