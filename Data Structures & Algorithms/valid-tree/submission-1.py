class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # If there is a cycle it is not a valid tree
        # Disconnected nodes == not valid
        if len(edges) > (n - 1): # Case: disconnected node, not enough edges to connect nodes
            return False
        
        adj = [[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()
        def dfs(node, par):
            if node in visit:
                return False
            
            visit.add(node)
            for nei in adj[node]:
                if nei == par: # since its undirected it has a reference back to the parent
                    continue # ignore it unless it comes back and has a node in visit
                if not dfs(nei, node): 
                    return False
            return True

        # when visit == n then we know all nodes have been visited
        return dfs(0, -1) and len(visit) == n