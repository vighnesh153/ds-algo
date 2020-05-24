def solve(arr):
    arr.sort()

    count = 0
    for i in range(2, len(arr)):
        side1_index = 0
        side2_index = i - 1

        while side1_index < side2_index:
            if arr[side1_index] + arr[side2_index] > arr[i]:
                count += side2_index - side1_index
                side2_index -= 1
            else:
                side1_index += 1

    return count


A = [2, 2, 3, 4]
print(solve(A))
