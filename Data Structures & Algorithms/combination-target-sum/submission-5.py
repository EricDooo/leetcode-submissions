class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort() # O(logn)
        path = []

        def dfs(i, totalsum): # O(n*2^n)
            if totalsum == target:
                res.append(path.copy()) # O(n)
                return 
            
            for j in range(i, len(nums)):
                if totalsum + nums[j] > target:
                    break 
                path.append(nums[j])
                dfs(j, totalsum+nums[j])
                path.pop()
        dfs(0, 0)
        return res
                