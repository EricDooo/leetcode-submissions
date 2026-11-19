class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def dfs(i):
            if i == len(nums) - 1: # reached the last index
                return True
            end = min(len(nums) - 1, i + nums[i]) # i + nums[i] is how many indexes from i we can jump
            for j in range(i + 1, end + 1): # it can jump from i+1 to nums[i]+1
                if dfs(j): # recursively call it, if it doesnt reach any of those, then its False
                    return True
            return False

        return dfs(0)