class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def helper(i, path):
            if len(path) == k:
                res.append(path.copy())
                return 
            if i > n:
                return
            
            #for i in range(1,n+1)
            if i not in path:
                path.append(i)
                take = helper(i + 1, path)
                path.pop()
            skip = helper(i + 1, path)
            return

        helper(1,[])
        return res
        
        