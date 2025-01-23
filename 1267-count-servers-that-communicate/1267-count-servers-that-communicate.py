class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        # topological sort?
        # check how many computers have a neighbor connected to them?
        rows = defaultdict(int)
        cols = defaultdict(int)

        servers = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    rows[row] += 1
                    cols[col] += 1
                    servers += 1

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    if rows[row] == 1 and cols[col] == 1:
                        servers -= 1
        return servers
        
        