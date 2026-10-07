# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(node, prevmax):
            if not node:
                return
            
            if node.val >= prevmax:
                nonlocal count
                count += 1
            
            dfs(node.left, max(prevmax, node.val))
            dfs(node.right, max(prevmax, node.val))
        dfs(root, float('-inf'))
        return count