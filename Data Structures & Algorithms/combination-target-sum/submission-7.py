class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        nums.sort()

        def dfs(i, total): # O(n*2^n)
            if total == target:
                res.append(path.copy()) # O(n)
                return
            
            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    return
                path.append(nums[j])
                dfs(j, total + nums[j])
                path.pop()
        dfs(0, 0)
        return res