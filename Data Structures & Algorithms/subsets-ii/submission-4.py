class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # O(nlogn)
        res = []
        subset = []

        def backtrack(i): # O(n*2^n)
            res.append(subset.copy())
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                subset.append(nums[j]) # Add the current number
                backtrack(j+1)

                subset.pop() # Remove the current number

        backtrack(0)
        return res