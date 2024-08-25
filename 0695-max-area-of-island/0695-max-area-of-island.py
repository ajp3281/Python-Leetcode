class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def in_bounds(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        def dfs(row, col, visited):
            area = 1
            visited.add((row,col))
            directions = [(-1,0), (0,-1), (1,0), (0,1)]
            for direction in directions:
                new_row, new_col = row + direction[0], col + direction[1]
                if in_bounds(new_row, new_col) and (new_row, new_col) not in visited and grid[new_row][new_col] == 1:
                    area += dfs(new_row, new_col, visited)
                    
            return area
        
        res = 0
        visited = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 and (row,col) not in visited:
                    res = max(res, dfs(row,col,visited))
                    
        return res
                    
        