from matrix_demo import Matrix
from cocktail_sort_demo import cocktail_sort


def matrix_to_sorted_list(matrix):
    flat_list = []
    for i in range(matrix.rows):
        for j in range(matrix.cols):
            flat_list.append(matrix.get(i, j))
    
    sorted_list, passes = cocktail_sort(flat_list)
    
    return sorted_list, passes


def sorted_list_to_matrix(sorted_list, rows, cols):
    data = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(sorted_list[i * cols + j])
        data.append(row)
    return Matrix(data)


def sort_matrix_elements(matrix):
    print("Original Matrix:")
    matrix.display()
    
    flat_list, passes = matrix_to_sorted_list(matrix)
    
    print(f"\nFlattened list: {flat_list}")
    print(f"Cocktail sort completed in {passes} passes")
    
    sorted_matrix = sorted_list_to_matrix(flat_list, matrix.rows, matrix.cols)
    
    print("\nSorted Matrix (row-major order):")
    sorted_matrix.display()
    
    return sorted_matrix


def sort_matrix_rows(matrix):
    print("Original Matrix:")
    matrix.display()
    
    sorted_data = []
    total_passes = 0
    
    for i in range(matrix.rows):
        row = [matrix.get(i, j) for j in range(matrix.cols)]
        sorted_row, passes = cocktail_sort(row)
        sorted_data.append(sorted_row)
        total_passes += passes
        print(f"\nRow {i+1} sorted: {sorted_row} (passes: {passes})")
    
    sorted_matrix = Matrix(sorted_data)
    print(f"\nTotal passes across all rows: {total_passes}")
    print("\nMatrix with each row sorted:")
    sorted_matrix.display()
    
    return sorted_matrix


def sort_matrix_columns(matrix):
    print("Original Matrix:")
    matrix.display()
    
    columns = []
    for j in range(matrix.cols):
        col = [matrix.get(i, j) for i in range(matrix.rows)]
        columns.append(col)
    
    sorted_columns = []
    total_passes = 0
    
    for j, col in enumerate(columns):
        sorted_col, passes = cocktail_sort(col)
        sorted_columns.append(sorted_col)
        total_passes += passes
        print(f"\nColumn {j+1} sorted: {sorted_col} (passes: {passes})")
    
    sorted_data = [[0] * matrix.cols for _ in range(matrix.rows)]
    for j in range(matrix.cols):
        for i in range(matrix.rows):
            sorted_data[i][j] = sorted_columns[j][i]
    
    sorted_matrix = Matrix(sorted_data)
    print(f"\nTotal passes across all columns: {total_passes}")
    print("\nMatrix with each column sorted:")
    sorted_matrix.display()
    
    return sorted_matrix


if __name__ == "__main__":
    print("=" * 60)
    print("Combined: Matrix + Cocktail Sort Demo")
    print("=" * 60)
    
    test_matrix = Matrix([[5, 2, 8], [1, 9, 3], [7, 4, 6]])
    
    print("\n" + "-" * 40)
    print("1. Sort all elements in matrix")
    print("-" * 40)
    sort_matrix_elements(test_matrix)
    
    print("\n" + "-" * 40)
    print("2. Sort each row individually")
    print("-" * 40)
    test_matrix2 = Matrix([[5, 2, 8], [1, 9, 3], [7, 4, 6]])
    sort_matrix_rows(test_matrix2)
    
    print("\n" + "-" * 40)
    print("3. Sort each column individually")
    print("-" * 40)
    test_matrix3 = Matrix([[5, 2, 8], [1, 9, 3], [7, 4, 6]])
    sort_matrix_columns(test_matrix3)

