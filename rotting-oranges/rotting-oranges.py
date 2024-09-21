class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # add all rotten oranges to visited and q
        # add al fresh oranges to need_to_visit
        # if len(need_to_visit) == 0 return time
        # if couldnt reach all fresh oranges, return -1
        def in_bounds(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        visited = set()
        need_to_visit = set()
        q = deque()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    visited.add((row,col))
                    q.append((row,col,0))
                elif grid[row][col] == 1:
                    need_to_visit.add((row,col))
                    
        if len(need_to_visit) == 0:
            return 0
           
        directions = [(-1,0), (0,-1), (1,0), (0,1)]
        while q:
            
            current_row, current_col, time = q.popleft()
            for direction in directions:
                new_row, new_col = current_row + direction[0], current_col + direction[1]
                if in_bounds(new_row, new_col) and (new_row, new_col) in need_to_visit:
                    q.append((new_row, new_col, time + 1))
                    need_to_visit.remove((new_row, new_col))
                    
                    if len(need_to_visit) == 0:
                        return time + 1
        return -1
            
                
        