class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [[x**2+y**2, [x,y]] for x,y in points]
        heapq.heapify(heap) #O(n)
        res = []

        while k > 0:
            _, coords = heapq.heappop(heap) # O(logn)
            res.append(coords)
            k -= 1
        return res