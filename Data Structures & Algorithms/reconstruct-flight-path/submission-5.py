class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dst in sorted(tickets):
            adj[src].append(dst)

        res = ["JFK"]
        def dfs(src):
            if len(res) == len(tickets) + 1: # found
                return True
            if src not in adj: # return back to backtrack
                return False

            temp = list(adj[src])
            for i, v in enumerate(temp):
                adj[src].pop(i)
                res.append(v)
                if dfs(v): return True
                adj[src].insert(i, v) # Restore flight back
                res.pop()
            return False

        dfs("JFK")
        return res