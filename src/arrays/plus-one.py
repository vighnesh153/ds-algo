def solve(arr):
    carry = 1
    for i in range(len(arr) - 1, -1, -1):
        arr[i] += carry
        if arr[i] >= 10:
            arr[i] %= 10
            carry = 1
        else:
            carry = 0

    if carry == 1:
        arr.insert(0, carry)
    return arr


A = [9, 9, 9]
print(solve(A))
