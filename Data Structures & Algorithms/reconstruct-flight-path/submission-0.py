class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        # We only build it reverse sorted for pop() O(1), otherwise a queue would work too right?
        for src, dst in sorted(tickets)[::-1]:
            adj[src].append(dst)
        res = []
        def dfs(src):
            while adj[src]:
                dst = adj[src].pop()
                dfs(dst)
            res.append(src)

        dfs('JFK')
        return res[::-1]