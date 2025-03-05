class Solution:
    def coloredCells(self, n: int) -> int:
        '''
        # brute force is bfs from border and return len(q) at minute
        directions = [(-1,0), (0,-1), (1,0), (0,1)]
        q = deque([(0, 0,0)])

        visited = set()
        cur_minute = 0
        while cur_minute < n:
            cur_minute, row, col = q.popleft()
            visited.add((row, col))

            for direction in directions:
                new_row, new_col = row + direction[0], col + direction[1]

                if (new_row, new_col) not in visited: 
                    q.append((cur_minute + 1, new_row, new_col))
        
        print(visited)
        print(q)
        return len(visited)
        '''

        # check how many neighbors we add at every turn
        
        # 1 = 1, 2 = 5, 3 = 13, 4 = 25, 41
        cur = 1
        prev_added = 0
        running_sum = 1
        while cur < n:
            prev_added += 4
            running_sum += prev_added
            cur += 1

        return running_sum