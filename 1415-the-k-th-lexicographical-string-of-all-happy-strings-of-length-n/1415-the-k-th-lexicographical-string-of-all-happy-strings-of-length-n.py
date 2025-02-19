class Solution:
    def getHappyString(self, n: int, k: int) -> str:

        # backtracking
        # take elem if not equal to prev
        # append it to res if length of path == n
        res = []
        elems = ['a', 'b', 'c']

        def backtrack(idx, path):
            if len(path) == n:
                res.append(path.copy())
                return
                
            if len(res) < k:
                for i in range(3):
                    if elems[i] != path[idx]:
                        path.append(elems[i])
                        backtrack(idx + 1, path)
                        path.pop()

        for i in range(3):
            backtrack(0, [elems[i]])
        
        print(res)
        if len(res) >= k:
            return ''.join(res[k-1])
        return ""
        