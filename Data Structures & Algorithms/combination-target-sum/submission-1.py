class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, path = [], []
        nums.sort()
        def dfs(i, total):
            if total == target:            # success
                res.append(path.copy())
                return
            if total > target:            # dead end
                return
            for j in range(i, len(nums)):
                path.append(nums[j])            # choose
                dfs(j, total+nums[j])
                path.pop()            # undo
        dfs(0, 0)
        return res