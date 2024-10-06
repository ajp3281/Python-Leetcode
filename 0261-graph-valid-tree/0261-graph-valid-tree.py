class UnionFind:
    def __init__(self, n):
        self.par = {}
        for i in range(n):
            self.par[i] = i
            
    def find(self, n):
        if n == self.par[n]:
            return n
        self.par[n] = self.find(self.par[n])
        return self.par[n]
    
    def union(self, n1, n2):
        par1 = self.find(n1)
        par2 = self.find(n2)
        
        if par1 == par2:
            return False
        else:
            self.par[par1] = par2
        return True
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # component count must be 0
        # no cycles
        uf = UnionFind(n)
        print(uf.par)
        for edge in edges:
            if not uf.union(edge[0], edge[1]):
                return False
            
        components = set()
        for i in range(n):
            components.add(uf.find(i))
        if len(components) == 1:
            return True
        return False
            
        