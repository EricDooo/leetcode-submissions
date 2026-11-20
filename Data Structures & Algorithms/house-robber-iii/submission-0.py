# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        stack = [(root, False)]
        results = []
        while stack:
            node, children_done = stack.pop()

            if node is None:
                results.append((0, 0))
            elif not children_done:
                stack.append((node,True))
                stack.append((node.right,False))
                stack.append((node.left,False))
            else:
                right = results.pop()
                left = results.pop()
                print(node.val, right, left)
                take, skip = node.val + left[1] + right[1], max(left) + max(right)
                results.append((take, skip))
        return max(results.pop())