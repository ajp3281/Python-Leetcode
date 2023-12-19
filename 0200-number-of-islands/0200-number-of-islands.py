class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        def bfs(r, c):
            q = deque()
            q.append((r,c))
            
            while q:
                currentrow, currentcol = q[0]
                q.popleft()
                
                if (currentrow+1 < len(grid) and grid[currentrow+1][currentcol] == "1" and (currentrow+1,currentcol) not in visited):
                    q.append((currentrow+1,currentcol))
                    visited.add((currentrow+1,currentcol))
                    
                if (currentrow-1 >= 0 and grid[currentrow-1][currentcol] == "1" and (currentrow-1,currentcol) not in visited):
                    q.append((currentrow-1,currentcol))
                    visited.add((currentrow-1,currentcol))
                    
                if (currentcol+1 < len(grid[0]) and grid[currentrow][currentcol+1] == "1" and (currentrow,currentcol+1) not in visited):
                    q.append((currentrow,currentcol+1))
                    visited.add((currentrow,currentcol+1))
                    
                if (currentcol-1 >= 0 and grid[currentrow][currentcol-1] == "1" and (currentrow,currentcol-1) not in visited):
                    q.append((currentrow,currentcol-1))
                    visited.add((currentrow,currentcol-1))
                    
                visited.add((currentrow,currentcol))
                
                    
                
        
        
        
        res = 0
        
        r,c = len(grid),len(grid[0])
        for i in range(r):
            for j in range(c):
                if (i,j) not in visited and grid[i][j] == "1":
                    bfs(i,j)
                    res += 1
                    
         
        return res
        