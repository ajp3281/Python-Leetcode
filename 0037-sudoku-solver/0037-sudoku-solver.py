class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        # backtracking solution
        # how to check if board is filled?
        
        visited_rows = [set() for _ in range(len(board))] 
        visited_cols = [set() for _ in range(len(board[0]))] 
        subgrids = [set() for _ in range(len(board))]
        
        need_to_fill = 0
        for row in range(len(board)):
            for col in range(len(board[0])):
                subgrid_index = (row // 3 * 3) + (col // 3)
                if board[row][col] == '.':
                    need_to_fill += 1
                else:
                    visited_rows[row].add(board[row][col])
                    visited_cols[col].add(board[row][col])
                    subgrids[subgrid_index].add(board[row][col])
                    
        
        
        def backtrack(row, col, visited_rows, visited_cols, subgrids,current_filled):
            if current_filled == need_to_fill:
                return True 
            
            if board[row][col] != ".":
                if col == 8:
                    return backtrack(row + 1, 0, visited_rows, visited_cols, subgrids, current_filled)
                else:
                    return backtrack(row, col + 1, visited_rows, visited_cols, subgrids, current_filled)
                
            subgrid_index = (row // 3 * 3) + (col // 3)
            for i in range(1,len(board)+1):
                num_str = str(i)
                if num_str not in visited_rows[row] and num_str not in visited_cols[col] and num_str not in subgrids[subgrid_index]:
                    board[row][col] = num_str
                    visited_rows[row].add(num_str)
                    visited_cols[col].add(num_str)
                    subgrids[subgrid_index].add(num_str)
                    if col == 8:
                        if backtrack(row + 1, 0, visited_rows, visited_cols, subgrids, current_filled + 1):
                            return True
                    else:
                        if backtrack(row, col+1, visited_rows, visited_cols, subgrids, current_filled + 1):
                            return True
                    board[row][col] = "."
                    visited_rows[row].remove(num_str)
                    visited_cols[col].remove(num_str)
                    subgrids[subgrid_index].remove(num_str)
            return False 
            
        
        backtrack(0,0, visited_rows, visited_cols, subgrids, 0)
            
            
            
            
            
            
        