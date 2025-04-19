import numpy as np

def get_matrix(rows, cols, name):
    """Get matrix input from user."""
    print(f"Enter values for {name} ({rows}x{cols}):")
    matrix = []
    for i in range(rows):
        row = list(map(float, input(f"Row {i + 1}: ").split()))
        if len(row) != cols:
            print(f"Error: You must enter exactly {cols} values for this row.")
            return get_matrix(rows, cols, name)
        matrix.append(row)
    return np.array(matrix)

def display_multiplication_step(matrix1, matrix2):
    """Display the step-by-step multiplication process."""
    rows1, cols1 = matrix1.shape
    rows2, cols2 = matrix2.shape
    print("\nStep-by-step multiplication:")
    result = np.zeros((rows1, cols2))

    for i in range(rows1):
        for j in range(cols2):
            elements_to_multiply = [(matrix1[i][k], matrix2[k][j]) for k in range(cols1)]
            print(f"Calculating result[{i + 1}][{j + 1}] by multiplying:")
            for a, b in elements_to_multiply:
                print(f"{a} * {b}")
        result[i][j] = sum(a * b for a, b in elements_to_multiply)
        print(f"Result[{i + 1}][{j + 1}] = {result[i][j]}\n")

    return result

def main():
    print("Matrix Multiplication Demonstration")

    # Get dimensions of matrices
    rows1 = int(input("Enter number of rows for Matrix A: "))
    cols1 = int(input("Enter number of columns for Matrix A: "))
    rows2 = int(input("Enter number of rows for Matrix B: "))
    cols2 = int(input("Enter number of columns for Matrix B: "))

    # Ensure matrices can be multiplied (columns of A == rows of B)
    if cols1 != rows2:
        print("Error: Number of columns in Matrix A must equal number of rows in Matrix B.")
        return

    # Get matrices from user
    matrix_a = get_matrix(rows1, cols1, "Matrix A")
    matrix_b = get_matrix(rows2, cols2, "Matrix B")

    # Display matrices
    print("\nMatrix A:")
    print(matrix_a)

    print("\nMatrix B:")
    print(matrix_b)

    # Display multiplication process and calculate result
    result_matrix = display_multiplication_step(matrix_a, matrix_b)

    # Display final result
    print("\nFinal Resultant Matrix:")
    print(result_matrix)

if __name__ == "__main__":
    main()