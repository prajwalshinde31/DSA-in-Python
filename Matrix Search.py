def d_search(matrix, target):
    row = 0
    col = len(matrix[0]) - 1

    while row < len(matrix) and col >= 0:
        num = matrix[row][col]

        if num == target:
            return True
        elif target < num:
            col -= 1
        elif num > num:
            row += 1
    return False


def binary_search_2d(mat, target, row, high, low):

    while low <= high:
        mid = (high + low) // 2

        if mat[row][mid] == target:
            return [row, mid]
        elif mat[row][mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return [-1, -1]


def sorted_matrix_search(mat, target):
    n = len(mat)
    m = len(mat[0])

    if n == 0:
        return [-1, -1]

    col_mid = m//2
    row_low = 0
    row_high = n-1

    while row_low+1 < row_high:

        row_mid = (row_low+row_high)//2

        if mat[row_mid][col_mid] == target:
            return [row_mid, col_mid]
        elif target > mat[row_mid][col_mid]:
            row_low = row_mid
        else:
            row_high = row_mid

    if mat[row_low+1][col_mid] == target:
        return [row_low+1][col_mid]
    elif mat[row_low][col_mid] == target:
        return [row_low, col_mid]
    elif mat[row_low][col_mid - 1] >= target >= mat[row_low][0]:
        return binary_search_2d(mat, target, row_low, col_mid-1, 0)
    elif mat[row_low+1][col_mid-1] >= target >= mat[row_low+1][0]:
        return binary_search_2d(mat, target, row_low+1, col_mid, 0)
    elif mat[row_low][col_mid+1] <= target <= mat[row_low][m-1]:
        return binary_search_2d(mat, target, row_low, m-1, col_mid+1)
    elif mat[row_low+1][col_mid+1] <= target <= mat[row_low+1][m-1]:
        return binary_search_2d(mat, target, row_low+1, m-1, col_mid+1)


matrix = [[0, 6, 8, 9, 11],
           [20, 22, 28, 29, 31],
           [36, 38, 50, 61, 63],
           [64, 66, 100, 122, 128]]
targ = 122
print(sorted_matrix_search(matrix, targ))
