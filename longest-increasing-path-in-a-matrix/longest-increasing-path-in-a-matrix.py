class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def in_bounds(row, col):
            return 0 <= row < len(matrix) and 0 <= col < len(matrix[0])
        
        
        def dfs(row, col, visited, memo):
            if (row,col) in memo:
                return memo[(row,col)]
            visited.add((row,col))
            res = 0
            directions = [(-1,0), (0,-1), (1,0), (0,1)]
            for direction in directions:
                new_row, new_col = row + direction[0], col + direction[1]
                
                if in_bounds(new_row, new_col) and (new_row, new_col) not in visited and matrix[new_row][new_col] > matrix[row][col]:
                    res = max(res, dfs(new_row, new_col, visited, memo) + 1)
                    
            visited.remove((row,col))
            memo[(row,col)] = res
            return res
        
        result = 0
        memo = {}
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                result = max(result, dfs(row, col, set(), memo)+1)
        return result