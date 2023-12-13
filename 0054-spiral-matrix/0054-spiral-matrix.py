class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        visited = []
        rowstart = 0
        colend = len(matrix[0])
        colstart = 0
        rowend = len(matrix)
        
        while (len(visited) < (len(matrix) * len(matrix[0]))):
            
            # top row
            for i in range(colstart,colend):
                visited.append(matrix[rowstart][i])
            rowstart += 1
            
            if colstart < colend:
                #rightmost col
                for i in range(rowstart,rowend):
                    visited.append(matrix[i][colend-1])
                colend -= 1
        
            
            #bottom col
            if rowstart < rowend:
                for i in reversed(range(colstart,colend)):
                    visited.append(matrix[rowend-1][i])
                rowend -= 1
            
            #leftmost col
            if colstart < colend:
                for i in reversed(range(rowstart,rowend)):
                    visited.append(matrix[i][colstart])
                colstart += 1
            
        return visited
            
            
            

            
            
                
            
        