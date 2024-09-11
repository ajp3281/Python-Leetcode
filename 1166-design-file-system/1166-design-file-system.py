class UnionFind():
    def __init__(self):
        self.par = {}
        self.rank = {}
        
    def find(self, n1):
        if self.par[n1] == n1:
            return n1
        self.par[n1] = self.find(self.par[n1])
        return self.par[n1]
    
    def union(self, n1, n2):
        if n1 not in self.par:
            self.par[n1] = n1
            self.rank[n1] = 1
        if n2 not in self.par:
            self.par[n2] = n2
            self.rank[n2] = 1
            
        par1, par2 = self.find(n1), self.find(n2)
        if par1 == par2:
            return False
        if self.rank[par1] > self.rank[par2]:
            self.par[par2] = par1
        elif self.rank[par2] > self.rank[par1]:
            self.par[par1] = par2
        else:
            self.par[par2] = par1
            self.rank[par1] = self.rank[par1] + 1
class FileSystem:

    def __init__(self):
        self.union = UnionFind()
        self.map = {}

    def createPath(self, path: str, value: int) -> bool:
        paths = path.split("/")  # Correct splitting of the path
        # Check if the parent exists
        if len(paths) > 1:
            parent = "/".join(paths[:-1])
            if parent and parent not in self.map:  # Parent must exist
                return False
        
        # Ensure we are not overwriting an existing path
        if path in self.map:
            return False
        
        # Add to union-find and map
        if len(paths) > 1:
            parent = "/".join(paths[:-1])
            self.union.union(parent, path)  # Link the path with its parent

        self.map[path] = value
        return True

    def get(self, path: str) -> int:
        if path in self.map:
            return self.map[path]
        else:
            return -1
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)