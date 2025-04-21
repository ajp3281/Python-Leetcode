class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first find row it exists in
        # then binary search the column

        # check if its less than 1st val of mid row, or greater than last val of mid row

        l = 0
        r = len(matrix)-1
        flag = False

        while l <= r:
            
            mid = (r + l) // 2

            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                flag = True
                break

            if target > matrix[mid][-1]:
                l = mid + 1
            else:
                r = mid - 1

        # how can we verify we found 
        if not flag:
            return False

        l = 0
        r = len(matrix[0])

        while l <= r:

            middle = (r+l) // 2

            if matrix[mid][middle] == target:
                return True
            
            if target > matrix[mid][middle]:
                l = middle + 1
            else:
                r = middle - 1

        return False

            
