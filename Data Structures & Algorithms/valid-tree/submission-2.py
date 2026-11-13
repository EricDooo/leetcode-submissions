class DSU:
    def __init__(self,n : int):
        self.comps = n
        self.Parent = list(range(n+1))
        self.Size = [1] * (n+1)
    
    def find(self, node):
        if self.Parent[node] != node:                           # node isn't a root
            self.Parent[node] = self.find(self.Parent[node])    # point it straight at its root
        return self.Parent[node]                                # the root

    def union(self, u, v):
        parentu, parentv = self.find(u), self.find(v)
        if parentu == parentv:
            return False # same root: already one group, so this edge is a cycle
        self.comps -= 1  # two groups become one
        if self.Size[parentu] < self.Size[parentv]:
            parentu, parentv = parentv, parentu   # parentu = root of the bigger group
        self.Size[parentu] += self.Size[parentv]  # bigger group absorbs the smaller's size
        self.Parent[parentv] = parentu            # the merge: smaller root goes under bigger root
        return True

    def components(self):
        return self.comps

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        
        dsu = DSU(n)
        for u,v in edges:
            if not dsu.union(u,v):
                return False
        return dsu.components() == 1 # if theres more than one group, disconnected