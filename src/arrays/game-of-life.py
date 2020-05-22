def get_alive_neighbors(arr, i, j):
    count = 0
    rows = len(arr)
    cols = len(arr[0])
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            if (x, y) == (0, 0):
                continue
            if 0 <= i + x < rows and 0 <= j + y < cols:
                count += arr[i + x][j + y] % 2
    return count


def solve(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            current_val = arr[i][j] % 2
            neighbors = get_alive_neighbors(arr, i, j)

            if current_val == 0:
                if neighbors == 3:
                    arr[i][j] = 2 + 0
                else:
                    arr[i][j] = 0
            elif current_val == 1:
                if neighbors in (2, 3):
                    arr[i][j] = 2 + 1
                else:
                    arr[i][j] = 0 + 1

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            arr[i][j] //= 2


A = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1],
    [0, 0, 0]
]
solve(A)
for row in A:
    print(row)
