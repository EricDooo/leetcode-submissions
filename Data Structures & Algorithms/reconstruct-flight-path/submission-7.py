class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        res = []
        adj = defaultdict(deque) # Store all tickets by sorted order
        # Post Order, we popleft from queue
        for src, dst in sorted(tickets):
            adj[src].append(dst)
        
        def dfs(src):
            while adj[src]:
                dst = adj[src].popleft()
                dfs(dst)
            res.append(src)
        
        dfs("JFK")
        return res[::-1]
