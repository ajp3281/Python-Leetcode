class NumMatrix:
    # prefix for every row
    # result += col2 - (col1 - 1) for every row in range 
    def __init__(self, matrix: List[List[int]]):
        self.prematrix = []
        for row in range(len(matrix)):
            current_row = [matrix[row][0]]
            for col in range(1, len(matrix[row])):
                current_row.append(current_row[-1] + matrix[row][col])
            self.prematrix.append(current_row)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for row in range(row1, row2 + 1):
            if col1 > 0:
                res += self.prematrix[row][col2] - self.prematrix[row][col1 - 1]
            else:
                res += self.prematrix[row][col2]

        return res

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)