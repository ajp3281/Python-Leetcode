class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        # maybe use hashmap for visited - keep track of how many times we've been on square?
        def in_bounds(row,col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        def dfs(row, col, visited):
            if row == end_row and col == end_col:
                if len(visited) == count+1:
                    return 1
            
            visited.add((row,col))
            directions = [(1,0), (0,1), (-1,0), (0,-1)]
            res = 0
            for direction in directions:
                new_row, new_col = row + direction[0], col + direction[1]
                if (new_row, new_col) not in visited and in_bounds(new_row, new_col) and grid[new_row][new_col] != -1:
                    res += dfs(new_row, new_col, visited)
            visited.remove((row,col))
            return res
            
            
        
        
        
        start_row = 0
        start_col = 0
        end_row = 0
        end_col = 0
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    start_row = row
                    start_col = col
                if grid[row][col] == 2:
                    end_row = row
                    end_col = col
                if grid[row][col] == 0:
                    count += 1
        print(count)
                    
        return dfs(start_row, start_col, set())
                