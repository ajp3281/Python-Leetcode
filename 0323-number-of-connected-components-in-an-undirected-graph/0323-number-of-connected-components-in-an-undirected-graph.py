class UnionFind:
    def __init__(self, n):
        self.par = {}
        self.rank = {}

        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0

    def find(self, n):
        if self.par[n] == n:
            return n
        par = self.par[n]
        self.par[n] = self.find(par)
        return self.par[n]

    def union(self, n1, n2):
        par1, par2 = self.find(n1), self.find(n2)

        if self.rank[par1] > self.rank[par2]:
            self.par[par2] = par1
            self.rank[par1] += 1
        elif self.rank[par1] < self.rank[par2]:
            self.par[par1] = par2
            self.rank[par2] += 1
        else:
            self.par[par2] = par1
            self.rank[par1] += 1

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        uf = UnionFind(n)

        for edge in edges:
            uf.union(edge[0], edge[1])

        print(uf.par)
        return len(set(uf.par.values()))
        