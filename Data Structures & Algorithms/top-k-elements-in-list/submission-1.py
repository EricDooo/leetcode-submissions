class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1

        freq = [[] for _ in range(len(nums)+1)]
        
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        res = []
        topk = 0
        for i in range(len(freq)-1, -1, -1):
            for num in freq[i]:
                res.append(num)
                topk += 1
                if topk == k:
                    return res
        return []