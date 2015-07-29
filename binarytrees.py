__author__ = 'sjoseph4'


class Node():
    def __init__(self, value):

        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):

        if value < self.value:

            if self.left:
                self.left.insert(value)
            else:
                self.left = Node(value)

        else:

            if self.right:
                self.right.insert(value)
            else:
                self.right = Node(value)

    def search(self, value):

        if self.value == value:
            return self

        if value < self.value:
            self.left.search(value)

        if value > self.value:
            self.right.search(value)


def dfs(tree, result=[]):
    if tree.left:
        dfs(tree.left, result)

    result.append(tree.value)

    if tree.right:
        dfs(tree.right, result)

    return result


def bfs(tree):
    queue = [tree]
    visited = []

    while queue:
        t = queue.pop(0)

        if t.left:
            queue.append(t.left)

        visited.append(t.value)

        if t.right:
            queue.append(t.right)

    return visited


def dfs_iterative(tree):
    queue = [tree]
    visited = []

    while queue:
        t = queue.pop()

        # check if leaf node
        if isinstance(t, int):
            visited.append(t)
            continue

        if t.right:
            queue.append(t.right)

        queue.append(t.value)

        if t.left:
            queue.append(t.left)

    return visited


values = [5, 3, 6, 10, 8]
root = values.pop()
bt = Node(root)

for val in values:
    bt.insert(val)

assert(dfs(bt) == [3, 5, 6, 8, 10])
assert(bfs(bt) == [8, 5, 10, 3, 6])
assert(dfs_iterative(bt) == [3, 5, 6, 8, 10])




