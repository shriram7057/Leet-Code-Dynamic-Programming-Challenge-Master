class Solution:
    def rob(self, root):
        def dfs(node):
            if not node:
                return (0, 0)

            left_rob, left_not = dfs(node.left)
            right_rob, right_not = dfs(node.right)

            # If we rob this node, we cannot rob children
            rob = node.val + left_not + right_not

            # If we don't rob this node, we can choose best of children
            not_rob = max(left_rob, left_not) + max(right_rob, right_not)

            return (rob, not_rob)

        return max(dfs(root))
