class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        pick = [False] * len(nums)

        def dfs(pick):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            for i in range(len(nums)):
                if not pick[i]:
                    path.append(nums[i])
                    pick[i] = True
                    dfs(pick)
                    path.pop()
                    pick[i] = False
        
        dfs(pick)
        return res