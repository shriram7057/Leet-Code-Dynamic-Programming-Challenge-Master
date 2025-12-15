class Solution:
    def maxPathSum(self, root):
        self.ans = float('-inf')

        def dfs(node):
            if not node:
                return 0

            # Max path sum from left/right child (ignore negative paths)
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            # Path passing through current node
            self.ans = max(self.ans, node.val + left + right)

            # Return max path going down
            return node.val + max(left, right)

        dfs(root)
        return self.ans
