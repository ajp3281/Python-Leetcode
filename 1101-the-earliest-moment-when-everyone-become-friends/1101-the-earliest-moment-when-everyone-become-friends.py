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
        self.par[n] = self.find(self.par[n])
        return self.par[n]
    
    def union(self, n1, n2):
        par1 = self.find(n1)
        par2 = self.find(n2)
        
        if par1 != par2:
            self.par[par2] = par1
    
class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        
        # union-find problem for sure
        # add edge for log in logs
        # union every edge
        # check if all nodes share same parent and return timestamp if so
        # if we get through all logs and not all same paretn return -1
        uf = UnionFind(n)
        logs.sort()
        for log in logs:
            time = log[0]
            n1 = log[1]
            n2 = log[2]
            
            uf.union(n1,n2)
            boolean = True
            first_found = uf.find(0)
            for i in range(1,n):
                if uf.find(i) != first_found:
                    boolean = False
            print(uf.par)
            if boolean:      
                return time
                
            
        return -1
        
        