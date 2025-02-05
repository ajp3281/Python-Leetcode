class UnionFind:
    def __init__(self, n):
        self.par = {}
        self.rank = {}
        for i in range(1,n + 1):
            self.par[i] = i
            self.rank[i] = 0
    
    def find(self, n):
        if self.par[n] == n:
            return n
        self.par[n] = self.find(self.par[n])
        return self.par[n]

    def union(self, n1, n2):
        par1, par2 = self.find(n1), self.find(n2)
        if par1 == par2:
            return False
        if self.rank[par1] > self.rank[par2]:
            self.par[par2] = par1
            self.rank[par1] += 1
        elif self.rank[par2] > self.rank[par1]:
            self.par[par1] = par2
            self.rank[par2] += 1
        else:
            self.par[par1] = par2
            self.rank[par2] += 1
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))

        for edge in edges:
            if not uf.union(edge[0], edge[1]):
                return edge
        return -1