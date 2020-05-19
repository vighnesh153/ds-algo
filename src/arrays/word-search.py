def recursion(board, i, j, word, index, indices):
    if index >= len(word):
        return True

    if not (0 <= i < len(board)) or not (0 <= j < len(board[0])):
        return False

    if (i, j) in indices:
        return False

    if board[i][j] == word[index]:
        indices.add((i, j))

        if recursion(board, i + 1, j, word, index + 1, indices):
            return True
        if recursion(board, i - 1, j, word, index + 1, indices):
            return True
        if recursion(board, i, j + 1, word, index + 1, indices):
            return True
        if recursion(board, i, j - 1, word, index + 1, indices):
            return True

        indices.remove((i, j))

    return False


def solve(board, word):
    word = list(word)
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == word[0]:
                if recursion(board, i, j, word, 0, set()):
                    return True

    return False


A = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]
B = "ABCES"
print(solve(A, B))
