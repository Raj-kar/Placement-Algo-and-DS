pixel = [
    [1, 1, 1, 2, 1, 1, 1],
    [2, 2, 1, 2, 2, 1, 1],
    [0, 2, 2, 2, 1, 1, 1],
    [1, 1, 0, 2, 1, 2, 2],
    [1, 1, 2, 2, 1, 0, 0]
]

def fill_pixel(matrix, row, col, toFill, prevFill):
    rows = len(matrix)
    cols = len(matrix[0])

    if (row < 0 or row >= rows or col < 0 or col >= cols):
        return

    if matrix[row][col] != prevFill:
        return

    matrix[row][col] = toFill

    fill_pixel(matrix, row-1, col, toFill, prevFill)
    fill_pixel(matrix, row, col - 1, toFill, prevFill)
    fill_pixel(matrix, row+1, col, toFill, prevFill)
    fill_pixel(matrix, row, col + 1, toFill, prevFill)
    return matrix


print(fill_pixel(pixel, 2, 3, 3, 2))

'''
[
    [1, 1, 1, 3, 1, 1, 1],
    [3, 3, 1, 3, 3, 1, 1],
    [0, 3, 3, 3, 1, 1, 1],
    [1, 1, 0, 3, 1, 2, 2],
    [1, 1, 3, 3, 1, 0, 0]
] 
'''
