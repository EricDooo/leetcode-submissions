class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(ind, path, total):
            if total == target:
                res.append(path.copy())
                return

            for j in range(ind, len(nums)):
                if nums[j] + total > target:
                    break
                path.append(nums[j])
                dfs(j, path, total + nums[j])
                path.pop()
        
        dfs(0,[],0)
        return res