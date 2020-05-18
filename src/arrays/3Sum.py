def solve(arr):
    answer = []
    arr.sort()

    for i in range(len(arr) - 2):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        j = i + 1
        k = len(arr) - 1

        while j < k:
            s = arr[i] + arr[j] + arr[k]
            if s == 0:
                answer.append([arr[i], arr[j], arr[k]])
                while j + 1 < k - 1 and arr[j] == arr[j + 1] and arr[k] == arr[k - 1]:
                    j += 1
                    k -= 1
                j += 1
                k -= 1
            elif s > 0:
                k -= 1
            else:
                j += 1

    return answer


A = [-2, 0, 0, 2, 2]
print(solve(A))
