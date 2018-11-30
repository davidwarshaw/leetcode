#!/usr/bin/env python

# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.vals = set()
        self.index = 0
        def _dfs(node):
            if node.left:
                _dfs(node.left)
            self.vals.add(node.val)
            if node.right:
                _dfs(node.right)

        if root:
            _dfs(root)

        self.vals = list(self.vals)

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.index < len(self.vals)

    def next(self):
        """
        :rtype: int
        """
        next_val = self.vals[self.index] if self.hasNext() else None
        self.index += 1
        return next_val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())

root = TreeNode(5)
root.left = TreeNode(3)
root.left.left = TreeNode(1)
root.left.left.left = TreeNode(0)
root.left.left.right = TreeNode(2)
root.left.right = TreeNode(4)
root.right = TreeNode(7)
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)
root.right.right.right = TreeNode(9)
inputs = [root]
expecteds = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]

if __name__ == '__main__':
    for input, expected in zip(inputs, expecteds):
        i, actual = BSTIterator(input), []
        while i.hasNext():
            actual.append(i.next())
        print(f"input: {input}")
        print(f"expected: {expected}")
        print(f"actual: {actual}")
        print(f"{actual == expected}")
        print()
