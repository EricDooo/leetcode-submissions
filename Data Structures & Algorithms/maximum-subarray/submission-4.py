from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            curSum = max(nums[i], curSum + nums[i])
            res = max(res, curSum)

        return res