# Scaler problem
from collections import defaultdict
from sys import setrecursionlimit


setrecursionlimit(11000)


class Node:
    def __init__(self, i, w):
        self.i = i
        self.weight = w
        self.children = set()

    def __repr__(self):
        return str(self.i)


def build_tree(arr):
    nodes = [Node(i + 1, 0) for i in range(len(arr) + 1)]
    helper = defaultdict(dict)
    for n1, n2, weight in arr:
        node1 = nodes[n1 - 1]
        node2 = nodes[n2 - 1]
        node1.children.add(node2)
        node2.children.add(node1)
        helper[node1.i][node2.i] = weight
        helper[node2.i][node1.i] = weight

    def set_weights_tree(node, visited, parent=None):
        if node.i in visited:
            return
        visited.add(node.i)

        if parent is not None:
            node.weight = helper[node.i][parent.i]
            node.children.remove(parent)

        for child in node.children:
            set_weights_tree(child, visited, node)

    root = nodes[0]
    root.weight = 0
    set_weights_tree(root, set())
    return root


def set_count(root, parents, count):
    parents.append(root)
    for node in parents:
        count[node.i - 1] = (count[node.i - 1][0] + 1, node.weight)

    for child in root.children:
        set_count(child, parents, count)

    parents.pop()


def solve(n, arr, c):
    tree = build_tree(arr)
    count = [(0, 0) for _ in range(n)]

    set_count(tree, [], count)
    count.sort(key=lambda x: x[0] * x[1])

    while c:
        if count[-1][1] <= 0:
            break
        count.pop()
        c -= 1

    s = 0
    modulo = 1e9 + 7
    for item in count:
        s += item[0] * item[1]

    return s % modulo


res = solve(5, [
    [1, 2, -8],
    [2, 3, -7],
    [3, 4, 5],
    [3, 5, -9],
], 4)
print(int(res))
