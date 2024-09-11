class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        
        def in_bounds(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        def dfs(row, col, visited):
            
            res = grid[row][col]
            visited.add((row,col))
            
            directions = [(-1,0), (0,-1), (1,0), (0,1)]
            
            
            for direction in directions:
                new_row = row + direction[0]
                new_col = col + direction[1]
                
                if (new_row, new_col) not in visited and in_bounds(new_row, new_col) and grid[new_row][new_col] > 0:
                    res += dfs(new_row, new_col, visited)
            
            return res
        
        result = 0
        visited = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row,col) not in visited and grid[row][col] != 0:
                    result = max(result, dfs(row,col,visited)) 
        return result
        