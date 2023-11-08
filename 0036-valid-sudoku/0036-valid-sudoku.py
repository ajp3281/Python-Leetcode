class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # hash table for each row
        # hash table for each col
        # hash table for each 3x3 grid
        
        # 
        # (row / 3)*3 + (col/3)
        # 5,5
        # 1*3 + 4
        rows = [set() for _ in range(len(board))]
        cols = [set() for _ in range(len(board))]
        subbox = [set() for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == ".":
                    continue
                elif ((board[i][j] in rows[i]) or
                     (board[i][j] in cols[j]) or
                     (board[i][j] in subbox[((i//3) * 3) + (j//3)])):
                    return False
                else:
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    subbox[((i//3) * 3) + (j//3)].add(board[i][j])
        
        
        return True
        
        
                