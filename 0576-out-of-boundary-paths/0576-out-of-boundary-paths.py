class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
        def out_of_bounds(row, col):
            return row < 0 or row >= m or col < 0 or col >= n
        
        MOD = 10**9 + 7
        
        directions = [(-1,0), (0,-1), (1,0), (0,1)]
        def helper(current_row, current_col, moves, visited, memo):
            if (current_row, current_col, moves) in memo:
                return memo[(current_row, current_col, moves)]
            
            if out_of_bounds(current_row, current_col):
                memo[(current_row, current_col, moves)] = 1
                return 1
            if moves >= maxMove:
                memo[(current_row, current_col, moves)] = 0
                return 0
            
            res = 0
            for direction in directions:
                new_row, new_col = direction[0] + current_row, current_col + direction[1]
                res += helper(new_row, new_col, moves + 1, visited, memo)
                res %= MOD

            memo[(current_row, current_col, moves)] = res
            return res
        
        return helper(startRow, startColumn, 0, set(), {})
            
            
            
            