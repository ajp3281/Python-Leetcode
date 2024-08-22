class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def in_bounds(row,col):
            '''
            if 0 <= row < len(board) and 0 <= col < len(board[0]):
                return True
            return False
            '''
            return (0 <= row < len(board) and 0 <= col < len(board[0]))
        def helper(row, col, current, visited):
            current.append(board[row][col])
            if ''.join(current) == word:
                return True
            if len(current) > len(word):
                return False
            if current[len(current)-1] != word[len(current)-1]:
                return False
            
            directions = [(-1,0), (0,-1), (1,0), (0,1)]
            visited.add((row,col))
            for direction in directions:
                
                new_row, new_col = row + direction[0], col + direction[1]
                
                if in_bounds(new_row, new_col) and (new_row, new_col) not in visited:
                    if helper(new_row, new_col, current, visited):
                        return True
                    current.pop()
            visited.remove((row,col))
                    
            
            return False
            
        
        visited = set()
        for row in range(len(board)):
            for col in range(len(board[0])):
                if helper(row,col,[],visited):
                        return True
        return False
        