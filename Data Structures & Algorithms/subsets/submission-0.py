class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums): # Reach the leafnodes
                res.append(subset.copy())
                return
            subset.append(nums[i]) # Add the current number
            dfs(i+1)

            subset.pop() # Remove the current number
            dfs(i+1)
        
        dfs(0)
        return res
