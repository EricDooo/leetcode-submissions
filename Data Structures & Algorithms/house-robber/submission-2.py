class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: # Base cases empty
            return 0
        if len(nums) == 1: # only 1, rob it
            return nums[0]
            
        rob1, rob2 = 0, 0

        for num in nums:
            temp = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2