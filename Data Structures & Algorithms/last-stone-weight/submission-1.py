class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap =  [-s for s in stones] # Max Heap
        heapq.heapify(heap) # O(n)

        while len(heap) > 1: 
            first = heapq.heappop(heap) # O(logn)
            second = heapq.heappop(heap) # O(logn)

            if second > first:
                heapq.heappush(heap, first - second) # O(logn)
            
        if not heap:
            return 0
        return abs(heap[0])