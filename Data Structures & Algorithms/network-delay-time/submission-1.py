import collections
import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))

        inf = float("inf")
        dist = [inf] * (n + 1)  # Nodes are numbered 1 through n
        dist[k] = 0
        min_heap = [(0, k)]

        while min_heap:
            time, node = heapq.heappop(min_heap)
            if time != dist[node]:
                continue  # A faster route was found after this entry was pushed

            for neighbor, weight in edges[node]:
                arrival = time + weight
                if arrival < dist[neighbor]:
                    dist[neighbor] = arrival
                    heapq.heappush(min_heap, (arrival, neighbor))

        delay = max(dist[1:])
        return -1 if delay == inf else delay