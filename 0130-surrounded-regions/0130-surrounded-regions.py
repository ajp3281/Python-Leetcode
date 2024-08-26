class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # do dfs - keep track of all current visited Os
        # if end of board is reached during any point in DFS, dont replace
        # else do replace
        
        def in_bounds(row,col):
            return 0 <= row < len(board) and 0 <= col < len(board[0])
        
        def dfs(row, col, current_visited, islands):
            if board[row][col] == 'X':
                return True
            islands.add((row,col))
            current_visited.add((row,col))
            directions = [(-1,0), (0,-1), (1,0), (0,1)]
            for direction in directions:
                new_row, new_col = row + direction[0], col + direction[1]
                if not in_bounds(new_row, new_col):
                    return False
                elif (new_row, new_col) not in current_visited:
                    if not dfs(new_row, new_col, current_visited, islands):
                        return False
            return True
        
        def replace(islands):
            for row,col in islands:
                board[row][col] = 'X'
        
        visited = set()
        islands = set()
        for row in range(len(board)):
            for col in range(len(board[0])):
                if (row,col) not in visited and board[row][col] == 'O':
                    visited.add((row,col))
                    if dfs(row,col,set(), islands) == True:
                        print(row,col)
                        replace(islands)
                        print(islands)
                    islands.clear()