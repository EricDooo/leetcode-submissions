# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        def dfs(i, node):
            if not node:
                return

            if len(res) == i:
                res.append(node.val)

            dfs(i+1, node.right)
            dfs(i+1, node.left)

        dfs(0, root)
        return res