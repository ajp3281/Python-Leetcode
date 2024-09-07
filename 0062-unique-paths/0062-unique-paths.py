class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def in_bounds(row, col):
            return 0 <= row < m and 0 <= col < n
        
        def dfs(row, col, memo):
            if (row,col) in memo:
                return memo[(row,col)]
                
            if row == m - 1 and col == n - 1:
                return 1
            
            directions = [(0,1), (1,0)]
            res = 0
            for direction in directions:
                new_row, new_col = direction[0] + row, direction[1] + col
                if in_bounds(new_row, new_col):
                    res += dfs(new_row, new_col, memo) 
            memo[(row,col)] = res
            return res
                    
        
        return dfs(0,0, {})