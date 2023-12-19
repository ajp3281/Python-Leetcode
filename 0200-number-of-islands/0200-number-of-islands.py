class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        def dfs(r, c):
            
            if ((r,c) in visited or grid[r][c] == "0"):
                return
            
            visited.add((r,c))
            
            if (r + 1 < len(grid)):
                dfs(r+1,c)
            if r-1 >= 0:
                dfs(r-1,c)
            if c+1 < len(grid[0]):
                dfs(r,c+1)
            if c-1 >= 0:
                dfs(r,c-1)
                
        
        
        res = 0
        
        r,c = len(grid),len(grid[0])
        for i in range(r):
            for j in range(c):
                if (i,j) not in visited and grid[i][j] == "1":
                    print(i,j)
                    dfs(i,j)
                    #visited.add((i,j))
                    res += 1
                    
         
        return res
        