# expected time complexity: linear time and constant space


# Explanation: https://www.youtube.com/watch?v=9SnkdYXNIzM&t=799s
def solve(arr):
    has_one = False

    for i, elem in enumerate(arr):
        if elem == 1:
            has_one = True
        if elem > len(arr) or elem <= 0:
            arr[i] = 1

    for i, elem in enumerate(arr):
        arr[abs(elem) - 1] = -abs(arr[abs(elem) - 1])

    for i, elem in enumerate(arr):
        if i == 0 and not has_one:
            return 1
        else:
            if elem > 0:
                return i + 1

    return len(arr) + 1


A = [7, 8, 9, 11, 12]
print(solve(A))
