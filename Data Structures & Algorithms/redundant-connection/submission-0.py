class DSU:
    def __init__(self, n):
        self.parents = list(range(n+1))
        self.rank = [1] * (n+1)
    
    def find(self, node):
        if node != self.parents[node]:
            self.parents[node] = self.find(self.parents[node])
        return self.parents[node]
    
    def union(self, u, v):
        parentu = self.find(u)
        parentv = self.find(v)

        if parentu == parentv:
            return False
        
        if self.rank[parentu] < self.rank[parentv]:
            parentu, parentv = parentv, parentu
        self.rank[parentu] += self.rank[parentv]
        self.parents[parentv] = parentu
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges))

        for u, v in edges:
            if not dsu.union(u, v):
                return [u,v]
        return []
