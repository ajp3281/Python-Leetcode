class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        def in_bounds(row,col):
            return 0 <= row < len(heights) and 0 <= col < len(heights[0])
            
        q = deque([])
        pacific = set()
        visited = set()
        for i in range(len(heights[0])):
            q.append((0, i))
            visited.add((0,i))
            pacific.add((0,i))
        for i in range(len(heights)):
            q.append((i,0))
            visited.add((i,0))
            pacific.add((i,0))
            
        while q:
            row, col = q.popleft()
            pacific.add((row,col))
            directions = [(0,1), (1,0), (-1,0), (0,-1)]
            for direction in directions:
                new_row, new_col = direction[0] + row, direction[1] + col
                if in_bounds(new_row, new_col) and (new_row, new_col) not in visited and heights[new_row][new_col] >= heights[row][col]:
                    q.append((new_row, new_col))
                    visited.add((new_row, new_col))
        
        visited.clear()
        q.clear()
        atlantic = set()
        for i in range(len(heights[0])):
            q.append((len(heights)-1, i))
            visited.add((len(heights)-1, i))
            atlantic.add((len(heights)-1, i))
        for i in range(len(heights)):
            q.append((i, len(heights[0])-1))
            visited.add((i, len(heights[0])-1))
            atlantic.add((i, len(heights[0])-1))
        while q:
            row, col = q.popleft()
            print(row,col)
            atlantic.add((row,col))
            directions = [(0,1), (1,0), (-1,0), (0,-1)]
            for direction in directions:
                new_row, new_col = direction[0] + row, direction[1] + col
                #print(new_row, new_col)
                if in_bounds(new_row, new_col) and (new_row, new_col) not in visited and heights[new_row][new_col] >= heights[row][col]:
                    q.append((new_row, new_col))
                    visited.add((new_row, new_col))
        
        return list(atlantic & pacific)
        
            
            
        
            
        