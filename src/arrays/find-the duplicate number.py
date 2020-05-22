# it is like finding a cycle in a linked list
def solve(arr):
    slow = arr[0]
    fast = arr[arr[0]]

    while slow != fast:
        slow = arr[slow]
        fast = arr[arr[fast]]

    length_of_cycle = 1
    slow = arr[slow]
    while slow != fast:
        length_of_cycle += 1
        slow = arr[slow]

    slow = fast = arr[0]
    for _ in range(length_of_cycle):
        fast = arr[fast]

    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]

    return slow


A = [3, 1, 3, 4, 2]
print(solve(A))
