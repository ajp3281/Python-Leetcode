class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        visited = set()
        if grid[len(grid)-1][len(grid[0])-1] == 1:
            return -1
        q = deque([(0,0,1)])
        
        while q:
            row, col, dist = q.popleft()
            if row == len(grid)-1 and col == len(grid[0])-1:
                return dist
            
            if (row,col) not in visited and row in range(len(grid)) and col in range(len(grid[0])) and grid[row][col] == 0:
                q.append((row+1,col,dist+1))
                q.append((row,col+1,dist+1))
                q.append((row-1,col,dist+1))
                q.append((row,col-1,dist+1))
                q.append((row+1,col+1,dist+1))
                q.append((row-1,col+1,dist+1))
                q.append((row+1,col-1,dist+1))
                q.append((row-1,col-1,dist+1))
                
            visited.add((row,col))
                
                
        return -1
                
        