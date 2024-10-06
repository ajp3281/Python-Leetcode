class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        '''
        [[10,8]
        [10,8],
        [1,2],
        [10,3],
        [1,3],
        [6,3],
        [5,2]]
        '''
        directions = [(-1,0), (0,1), (1,0), (0,-1)]
        
        def in_bounds(row, col):
            return 0 <= row < len(heights) and 0 <= col < len(heights[0])
        heap = [(0, 0, 0)]
        heapq.heapify(heap)
        visited = {}
        while heap:
            effort, row, col = heapq.heappop(heap)
            
            if row == len(heights)-1 and col == len(heights[0])-1:
                return effort
            
            if (row,col) in visited:
                continue
            visited[(row,col)] = effort
            
            for direction in directions:
                new_row, new_col = row + direction[0], col + direction[1]
                
                if in_bounds(new_row, new_col) and (new_row, new_col) not in visited:
                    effort_required = max(effort, abs(heights[new_row][new_col] - heights[row][col]))
                    heapq.heappush(heap, (effort_required, new_row, new_col))
                    
        return -1
        
        
            
        