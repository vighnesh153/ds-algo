# Expected time complexity: O(log(m + n))


def solve(arr1, arr2):
    if len(arr1) > len(arr2):
        return solve(arr2, arr1)

    low = 0
    high = len(arr1)
    while low <= high:
        partition_x = (low + high) // 2
        partition_y = (len(arr1) + len(arr2) + 1) // 2 - partition_x

        max_left_x = -float('inf') if partition_x == 0 else arr1[partition_x - 1]
        min_right_x = float('inf') if partition_x == len(arr1) else arr1[partition_x]

        max_left_y = -float('inf') if partition_y == 0 else arr2[partition_y - 1]
        min_right_y = float('inf') if partition_y == len(arr2) else arr2[partition_y]

        if max_left_x <= min_right_y and max_left_y <= min_right_x:
            if (len(arr1) + len(arr2)) % 2 == 0:
                return (max(max_left_x, max_left_y) +
                        min(min_right_x, min_right_y)) / 2
            else:
                return max(max_left_x, max_left_y)
        elif max_left_x > min_right_y:
            high = partition_x - 1
        else:
            low = partition_x + 1
