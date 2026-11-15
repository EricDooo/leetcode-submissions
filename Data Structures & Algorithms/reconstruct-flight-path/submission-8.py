class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        res = []
        adj = defaultdict(list)
        for src, dst in sorted(tickets):
            adj[src].append(dst)
        
        res = ["JFK"]
        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in adj: # Flight doesnt exist
                return False

            temp = list(adj[src])
            for i,v in enumerate(temp):
                adj[src].pop(i)
                res.append(v)

                if dfs(v): return True # Path found travel back up

                adj[src].insert(i,v) # Backtrack
                res.pop() # False path backtrack
            return False
                

        dfs("JFK")
        return res