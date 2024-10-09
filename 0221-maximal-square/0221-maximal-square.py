class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        # what determines if we have a square?
        # diagonal + left/right + up/down in same direction?
        # how to check this?
        
        if not matrix or not matrix[0]:
            return 0
        
        # Initialize variables to keep track of the max square length
        maxsq = 0
        rows, cols = len(matrix), len(matrix[0])

        # Iterate through each cell in the matrix
        for i in range(rows):
            for j in range(cols):
                # Only update values for cells not in the first row or first column
                if matrix[i][j] == "1":
                    if i > 0 and j > 0:  # Skip first row and first column
                        # Calculate the size of the square ending at this cell
                        matrix[i][j] = str(min(int(matrix[i-1][j]), int(matrix[i][j-1]), int(matrix[i-1][j-1])) + 1)
                    maxsq = max(maxsq, int(matrix[i][j]))

        return maxsq * maxsq
        