class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(-1,0), (0,-1), (1,0), (0,1)]

        def in_bounds(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        def dfs(row, col):
            if (row,col) in visited or not in_bounds(row,col) or grid[row][col] == 0:
                return 0

            visited.add((row,col))
            current_perimeter = 0
            for direction in directions:
                new_row, new_col = row + direction[0], col + direction[1]
                if not in_bounds(new_row, new_col) or grid[new_row][new_col] == 0:
                    current_perimeter += 1

            return current_perimeter + dfs(row + 1, col) + dfs(row, col + 1) + dfs(row - 1, col) + dfs(row, col - 1)
        # find island - then find out how many non land cells it borders?
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(i,j)
