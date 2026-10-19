class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Here we use a heap due to how we can keep k of something in a storage in O(logk)

        heap = [(-(x**2 + y**2), [x,y]) for x,y in points]
        heapq.heapify(heap)
        while len(heap) > k:
            heapq.heappop(heap)
        
        res = [coords for _, coords in heap]

        return res