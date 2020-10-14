def path(row, column):
    '''find all the path of a n*m matrix'''
    if row == 1 or column == 1:
        return 1
    return path(row - 1, column) + path(row, column - 1)


print(path(4, 4))   # 20
print(path(200, 1))  # 1
print(path(2, 2))
