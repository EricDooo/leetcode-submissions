# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        if root is None:
            return 0

        stack = [(root, False)]
        results = {}

        while stack:
            node, expanded = stack.pop()

            if not expanded:
                stack.append((node, True))
                if node.right is not None:
                    stack.append((node.right, False))
                if node.left is not None:
                    stack.append((node.left, False))
                continue

            left_rob, left_skip = results.pop(node.left, (0, 0))
            right_rob, right_skip = results.pop(node.right, (0, 0))

            rob_node = node.val + left_skip + right_skip
            skip_node = max(left_rob, left_skip) + max(right_rob, right_skip)
            results[node] = (rob_node, skip_node)

        return max(results[root])