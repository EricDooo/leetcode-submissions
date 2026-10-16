class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort() # Sort so we can stop early

        def dfs(i, cur, total):
            if total == target: # return a copy when reached
                res.append(cur.copy())
                return
            
            for j in range(i, len(nums)):
                # Add and loop until target
                if total + nums[j] > target:
                    return
                cur.append(nums[j])
                dfs(j, cur, total+nums[j])
                # Reuse the same number into recursion
                cur.pop()
            
        dfs(0, [], 0)
        return res