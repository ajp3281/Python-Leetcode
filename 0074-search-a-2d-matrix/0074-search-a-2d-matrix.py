class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
         
        
        lcol = 0
        rcol = len(matrix)-1
        
        while lcol <= rcol:
            midcol = (lcol + rcol)//2

            if target >= matrix[midcol][0] and target <= matrix[midcol][len(matrix[0])-1]:
                break
            
            if target > matrix[midcol][len(matrix[0])-1]:
                lcol = midcol+1
                
            if target < matrix[midcol][0]:
                rcol = midcol-1
                
        
        l = 0
        r = len(matrix[midcol])-1
        
        while l <= r:
            mid = (l+r)//2
            if target > matrix[midcol][mid]:
                l = mid+1
            elif target < matrix[midcol][mid]:
                r = mid-1
            else:
                return True
        
        return False
                
        