class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:

        # we can brute force this
        # but how can we join ranges?

        # increase by 1 and decrease by one for left and right ptrs?

        # row1,col1 - row2, col2
        # row1[col1] += 1
        # [col2+1] -= 1
        mat = [[0] * n for _ in range(n)]
        #print(mat)
        for row1, col1, row2, col2 in queries:
            for i in range(row1, row2+1):
                mat[i][col1] += 1
                if col2 + 1 < n:
                    mat[i][col2+1] -= 1

        for row in range(len(mat)):
            for col in range(1,len(mat[0])):
                mat[row][col] += mat[row][col-1]
        return mat
            #print(mat)
        