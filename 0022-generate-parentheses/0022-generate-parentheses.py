class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        '''
        
        dp for sure
        if left count == right count : need left
        if left count < right count : can do either
        if left count == n and right < n : need right
        if left and right == n : valid case
        
        pseudo code
        dfs helper
        if left == n and right == n:
            add current path
        if left == n:
            add right
            
        '''
        res = []
        def dfs(left, right, path):
            if right > left or left > n or right > n:
                return
            if left == n and right == n:
                res.append(''.join(path.copy()))
            if left < n:
                path.append("(")
                dfs(left + 1, right, path)
                path.pop()
            if right < n:
                path.append(")")
                dfs(left, right + 1, path)
                path.pop()
            return
        
        dfs(0,0,[])
        return res
        