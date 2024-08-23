class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        # backtracking - place a queen at a certain spot, keep going down decision tree
        # to see if following queens can be placed at valid spot
        # if valid spot isnt possible , backtrack to previous queen
        
        # how to keep track of valid spot?
        # maybe once queen is placed, add it to placed queens, and calculate places where it cant be placed?
        def build_board(queens):
            # 1d array of 4 strings
            board = ["." * n for _ in range(n)]
            for queen in queens:
                row, col = queen
                board[row] = board[row][:col] + 'Q' + board[row][col+1:]
            return board

        
        def in_bounds(row,col):
            return (0 <= row < n and 0 <= col < n)
        
        def check_spot(row, col, queens):
            
            for queen in queens:
                current_queen_row, current_queen_col = queen
                if row == current_queen_row:
                    return False
                if col == current_queen_col:
                    return False
                
                directions = [(-1,-1), (1,1), (-1, 1), (1,-1)]
                for direction in directions:
                    queen_row = current_queen_row
                    queen_col = current_queen_col
                    while in_bounds(queen_row, queen_col):
                        if row == queen_row and col == queen_col:
                            return False
                        queen_row += direction[0]
                        queen_col += direction[1]
                        
            return True
        
        res = 0
        
        def dfs(row, col, queens):
            if not check_spot(row,col,queens):
                return False
            
            if row == n-1:
                queens.add((row,col))
                res.append(build_board(queens))
                queens.remove((row,col))

            queens.add((row,col))
            for j in range(n):
                if dfs(row + 1, j, queens):
                    return True
            queens.remove((row,col))
            return False
                
        res = []
        count = 0
        col = 0
        for col in range(n):
            dfs(0, col, set())

          
        return res
                        