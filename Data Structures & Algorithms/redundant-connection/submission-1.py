class DSU:
    def __init__(self, n):
        self.parents = list(range(n+1))
        self.rank = [1] * (n+1)
    
    def find(self, node):
        p = self.parents[node] 
        while p != self.parents[p]: # keeps going until p is its own parent == root
            self.parents[p] = self.parents[self.parents[p]] # p -> grandparent
            p = self.parents[p] # p moves to grandparent
        return p # node is now pointed to the root
        

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
