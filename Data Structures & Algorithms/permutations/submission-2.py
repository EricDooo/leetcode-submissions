class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        pick = [False] * len(nums)
        def dfs():
            if len(path) == len(nums):
                res.append(path.copy())
                return
            
            for i in range(len(nums)):
                if not pick[i]:
                    path.append(nums[i])
                    pick[i] = True
                    dfs()
                    path.pop() # Backtrack undo picking
                    pick[i] = False
        dfs()
        return res