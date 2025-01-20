class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:

        # hashmaps to keep track of visited for row and columns?
        # check if current painted row/col is all painted
        rows = []
        for i in range(len(mat)):
            rows.append(0)
        cols = []
        for j in range(len(mat[0])):
            cols.append(0)
        
        #print(rows, cols)
        pos = {}
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                pos[mat[i][j]] = (i,j)
        
        for i, num in enumerate(arr):
            row, col = pos[num]
            rows[row] += 1
            cols[col] += 1
            if rows[row] == len(mat[0]) or cols[col] == len(mat):
                return i
        
        # 4 3 5
        # 1 2 6
        return -1


        