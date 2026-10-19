class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [n for n in nums] # O(n) operation
        heapq.heapify(heap) # O(n) for heapify

        while len(heap) > k:
            heapq.heappop(heap) # O(logn)
        
        return heap[0]