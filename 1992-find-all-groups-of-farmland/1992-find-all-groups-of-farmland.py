class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        # dfs 

        directions = [(-1,0), (1,0), (0,1), (0,-1)]
        visited = set()

        def in_bounds(row, col):
            return 0 <= row < len(land) and 0 <= col < len(land[0])

        def dfs(row, col, visited):
            visited.add((row, col))

            for direction in directions:
                new_row, new_col = row + direction[0], col + direction[1]
                if (new_row, new_col) not in visited and in_bounds(new_row, new_col) and land[new_row][new_col] != 0:
                    dfs(new_row, new_col, visited)




        # we are always visiting top left position first
        # how to handle skipping neighbors and only going diagonal
        # we still need to return the rightmost diagonal
        # iterate thru visited set?
        res = []
        for i in range(len(land)):
            for j in range(len(land[0])):
                if (i,j) not in visited and land[i][j] == 1: 
                    dfs(i,j, visited)
                    end_row, end_col = i,j
                    while (end_row + 1, end_col) in visited:
                        end_row += 1 
                    while (end_row, end_col + 1) in visited:
                        end_col += 1
                    res.append([i,j,end_row,end_col])

        return res
        