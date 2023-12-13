class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
         # Transpose Matrix
        for row in range(len(matrix)):
            for col in range(row+1,len(matrix)):
                matrix[row][col],matrix[col][row] = matrix[col][row],matrix[row][col]
                
        print(matrix)
        
        #reverse rows
        for row in matrix:
            row.reverse()
                
        """
        Do not return anything, modify matrix in-place instead.
        """
        
                
                    
                    
                
                
        