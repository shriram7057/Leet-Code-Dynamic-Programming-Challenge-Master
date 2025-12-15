# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def generateTrees(self, n: int):
        if n == 0:
            return []

        def build(start, end):
            if start > end:
                return [None]

            trees = []
            for root in range(start, end + 1):
                leftTrees = build(start, root - 1)
                rightTrees = build(root + 1, end)

                for left in leftTrees:
                    for right in rightTrees:
                        node = TreeNode(root)
                        node.left = left
                        node.right = right
                        trees.append(node)

            return trees

        return build(1, n)
