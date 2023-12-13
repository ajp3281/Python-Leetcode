class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[1] * n  for _ in range(n)]
        if n == 1:
            return matrix
        rowstart = 0
        colstart = 0
        colend = n
        rowend = n
        
        count = 0
        while count < n*n:
            
            #build top row
            for i in range(colstart,colend):
                if count >= n*n:
                    return matrix
                matrix[rowstart][i] = count+1 
                count += 1
            rowstart += 1
            
    
            # build rightmost row
            for i in range(rowstart,rowend):
                if count >= n*n:
                    return matrix
                matrix[i][colend-1] = count+1
                count += 1
            colend -= 1

            # build bottom row
            for i in reversed(range(colstart,colend)):
                if count >= n*n:
                    return matrix
                matrix[rowend-1][i] = count+1
                count += 1
            rowend -= 1
            
            # built leftmost col
            for i in reversed(range(rowstart,rowend)):
                if count >= n*n:
                    return matrix
                matrix[i][colstart] = count+1
                count += 1
            colstart += 1
        
        return matrix
            
        
        
        
        