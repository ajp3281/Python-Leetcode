class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:

        # backtracking again
        # should we start with string of length n?
        # or start with 0 and start flipping?

        res = None
        start = list("0" * len(nums))
        visited = set(nums)

        def backtrack(idx, path):
            nonlocal res
            if ''.join(path) not in visited:
                res = ''.join(path)
                return 

            if not res:
                path[idx] = "1"
                backtrack(idx + 1, path)
                path[idx] = "0"
        
        backtrack(0, start)
        return res