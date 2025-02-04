class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]

        for r in range(1, len(self.prefix)):
            rowsum = 0
            for c in range(1, len(self.prefix[0])):
                rowsum += matrix[r-1][c-1]
                above = self.prefix[r-1][c]
                self.prefix[r][c] = rowsum + above



        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        targetval = self.prefix[row2+1][col2+1]
        left = self.prefix[row2 + 1][col1]
        above = self.prefix[row1][col2 + 1]
        duplicated = self.prefix[row1][col1]
        print(targetval, left, above, duplicated)
        return targetval - left - above + duplicated
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)