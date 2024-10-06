class UnionFind:
    def __init__(self):
        self.par = {}
    
    def find(self, node):
        if node not in self.par:
            self.par[node] = node
            return node
        
        if self.par[node] == node:
            return node
        self.par[node] = self.find(self.par[node])
        return self.par[node]
        
    def union(self, node1, node2):
        par1 = self.find(node1)
        par2 = self.find(node2)
        
        if par1 != par2:
            self.par[par1] = par2
        

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        # classic union find 
        # build parents graph and count how many unique parents there are
        
        # 0 - 1 - 2
        # 3 - 4
        uf = UnionFind()
        
        for edge in edges:
            uf.union(edge[0], edge[1])
            
        components = set()
        for i in range(n):
            components.add(uf.find(i))
            
        print(components)
        return len(components)
            
            
        
        