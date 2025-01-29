class UnionFind:
    
    def __init__(self, n):
        self.par = {}
        self.rank = {}
        
        for i in range(1,n+1):
            self.par[i] = i
            self.rank[i] = 0
            
    def find(self, n):
        if self.par[n] == n:
            return n
        else:
            return self.find(self.par[n])
    
    def union(self, n1, n2):
        parent1, parent2 = self.find(n1), self.find(n2)
        
        if parent1 == parent2:
            return False
        
        if self.rank[parent1] > self.rank[parent2]:
            self.par[parent2] = parent1
        elif self.rank[parent2] > self.rank[parent1]:
            self.par[parent1] = parent2
        else:
            self.par[parent2] = parent1
            self.rank[parent1] += 1
        return True
        
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        adj = defaultdict(list)
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
            
        maxval = len(edges)
        
        unionfind = UnionFind(maxval)
        for edge in edges:
            if not unionfind.union(edge[0], edge[1]):
                return edge
        
        return -1
        
        
        
        
        