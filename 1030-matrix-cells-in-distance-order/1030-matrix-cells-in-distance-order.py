class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        
        def getDistance(row1, col1, row2, col2):

            return (abs(row1 - row2) + abs(col1-col2))

        def in_bounds(row, col):
            return 0 <= row < rows and 0 <= col < cols

        directions = [(-1,0), (0,-1), (1,0), (0,1)]

        # so explore all cells and sort by distance?
        res = []
        heap = [(0, rCenter, cCenter)]
        visited = set()
        visited.add((rCenter, cCenter))
        heapq.heapify(heap)

        while heap:
            dist, cur_row, cur_col = heapq.heappop(heap)
            print(cur_row, cur_col)

            res.append((cur_row, cur_col))
            for direction in directions:
                new_row, new_col = cur_row + direction[0], cur_col + direction[1]
                if in_bounds(new_row, new_col) and (new_row, new_col) not in visited:
                    new_dist = getDistance(rCenter, cCenter, new_row, new_col)
                    heapq.heappush(heap, (new_dist, new_row, new_col))
                    visited.add((new_row, new_col))

        return res


    