class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        # preprocess all islands and store size of island in visited set

        # iterate thru 1s and count islands from all 4 directions

        def in_bounds(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        directions = [(-1,0), (0,-1), (1,0), (0,1)]

        sizes = {}
        islandcount = 2
        def dfs(row, col, islandcount):
            
            grid[row][col] = islandcount
            visited.add((row,col))

            for direction in directions:
                new_row, new_col = direction[0] + row, direction[1] + col

                if (in_bounds(new_row, new_col)) and (new_row, new_col) not in visited and grid[new_row][new_col] == 1:
                    dfs(new_row, new_col, islandcount)
            return


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] not in sizes and grid[i][j] == 1:
                    visited = set()
                    dfs(i,j, islandcount)

                    for row,col in visited:
                        sizes[(row,col)] = len(visited)
                    islandcount += 1

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == 0:
                    current = 1
                    visited = set()
                    for direction in directions:
                        new_row, new_col = direction[0] + i, direction[1] + j

                        if (new_row, new_col) in sizes and grid[new_row][new_col] not in visited:
                            visited.add(grid[new_row][new_col])
                            current += sizes[(new_row, new_col)]

                    res = max(res, current)
        if res == 0:
            return len(grid) * len(grid[0])
        return res            
