class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [(-(x**2 + y**2), x, y) for x,y in points]
        heap = []
        for d in distances:
            heapq.heappush(heap, d)
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for _,x,y in heap:
            res.append([x,y])
        
        return res
        
