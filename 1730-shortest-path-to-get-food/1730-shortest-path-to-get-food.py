class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        
        # find * location, append to q
        # bfs from there
        
        q = deque([])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "*":
                    q.append((i,j,0))
           
        def in_bounds(row,col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        visited = set()
        directions = [(-1,0), (0,-1), (1,0), (0,1)]
        while q:
            currentrow, currentcol, distance = q.popleft()
            if grid[currentrow][currentcol] == "#":
                return distance
            
            for direction in directions:
                newrow, newcol = currentrow + direction[0], currentcol + direction[1]
                if in_bounds(newrow, newcol) and grid[currentrow][currentcol] != "X":
                    q.append((newrow, newcol, distance + 1))
                    
            grid[currentrow][currentcol] = "X"
                    
        return -1
            
        
            
            
        