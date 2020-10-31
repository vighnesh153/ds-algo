# https://www.codechef.com/LTIME89B/problems/SUBMEXS

from sys import setrecursionlimit

# Default is around 900-1000
setrecursionlimit(110000)


class Node:
    def __init__(self):
        self.children = []
        self.subtree_children_count = 0


def post_order(node):
    count = 1

    for child in node.children:
        child_sub_trees = post_order(child)
        count += child_sub_trees

    node.subtree_children_count = count
    return node.subtree_children_count


def subtree_count(root):
    return post_order(root)


def assign_parents(parents, nodes):
    for i, parent in enumerate(parents, 1):
        nodes[parent].children.append(nodes[i + 1])


def get_submex(root):
    ans = -1

    def maximizer(node, prev=0):
        nonlocal ans

        value = node.subtree_children_count + prev
        ans = max(ans, value)

        for child in node.children:
            maximizer(child, value)

    maximizer(root)
    return ans


def solve():
    for _ in range(int(input())):
        n = int(input())
        parents = list(map(int, input().strip().split()))

        nodes = [Node() for _ in range(n + 1)]

        assign_parents(parents, nodes)

        root = nodes[1]
        subtree_count(root)
        result = get_submex(root)
        print(result)


solve()
