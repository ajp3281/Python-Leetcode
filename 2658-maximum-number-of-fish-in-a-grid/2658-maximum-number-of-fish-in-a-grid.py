class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        
        def in_bounds(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        def bfs(row, col, visited):
            visited.add((row,col))
            directions = [(1,0), (-1,0), (0,-1), (0,1)]

            q = deque([(row,col)])   
            res = 0
            while q:
                cur_row, cur_col = q.popleft()
                res += grid[cur_row][cur_col]

                for direction in directions:
                    new_row, new_col = cur_row + direction[0], cur_col + direction[1]
                    if in_bounds(new_row, new_col) and grid[new_row][new_col] > 0 and (new_row, new_col) not in visited:
                        visited.add((new_row, new_col))
                        q.append((new_row, new_col))
            return res
        
        result = 0
        visited = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row,col) not in visited and grid[row][col] != 0:
                    result = max(result, bfs(row,col,visited)) 
        return result
        