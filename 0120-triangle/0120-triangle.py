class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        def helper(row, col, current, memo):
            if (row,col) in memo:
                return memo[(row,col)]
            if row == len(triangle)-1:
                memo[(row,col)] = triangle[row][col]
                return triangle[row][col]
            
            left = helper(row + 1, col, current, memo)
            right = helper(row + 1, col + 1, current, memo)
            memo[(row,col)] = triangle[row][col] + min(left, right)
            return triangle[row][col] + min(left, right)
        
        return helper(0,0,0,{})