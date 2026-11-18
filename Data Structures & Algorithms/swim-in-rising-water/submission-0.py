import heapq
from typing import List

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        heap = [(grid[0][0], 0, 0)] # Initialize with smallest
        seen = {(0, 0)}
        time = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while heap:
            elevation, row, col = heapq.heappop(heap)
            time = max(time, elevation)

            if row == n - 1 and col == n - 1: # Base Case
                return time

            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                # bounds and if its in seen
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in seen:
                    seen.add((nr, nc))
                    heapq.heappush(heap, (grid[nr][nc], nr, nc))

        return time