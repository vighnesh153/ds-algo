def solve(arr):
    result = []
    local_result = []

    for i, elem in enumerate(arr):
        if i == 0:
            local_result.append(str(elem))
        else:
            if elem != arr[i - 1] + 1:
                result.append("->".join(local_result))
                local_result = [str(elem)]
            else:
                if len(local_result) == 1:
                    local_result.append(str(elem))
                else:
                    local_result[-1] = str(elem)

    if len(local_result) > 0:
        result.append('->'.join(local_result))

    return result


A = [0, 2, 3, 4, 6, 8, 9]
print(solve(A))
