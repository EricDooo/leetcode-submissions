class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = res = 0
        count = defaultdict(int)
        count[0] = 1
        
        for n in nums:
            prefix += n
            res += count[prefix - k]
            count[prefix] += 1
        return res