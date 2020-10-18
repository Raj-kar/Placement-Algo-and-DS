def count_island(arr, i, j):
    if i < 0 or i >= len(arr) or j < 0 or j >= len(arr[i]) or arr[i][j] == "0":
        return

    arr[i][j] = "0"

    count_island(arr, i, j-1)
    count_island(arr, i, j+1)
    count_island(arr, i+1, j)
    count_island(arr, i-1, j)


def solve(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == "1":
                count += 1
                count_island(arr, i, j)
    return count


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]

print(solve(grid))   # 1

grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

print(solve(grid))  # 3
