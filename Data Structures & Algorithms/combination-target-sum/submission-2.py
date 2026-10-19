class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, path = [], []
        nums.sort()
        def dfs(i, total):
            if total == target:            # success
                res.append(path.copy())
                return
            for j in range(i, len(nums)):
                if total + nums[j] > target:            # dead end
                    return
                path.append(nums[j])            # choose
                dfs(j, total+nums[j])
                path.pop()            # undo
        dfs(0, 0)
        return res