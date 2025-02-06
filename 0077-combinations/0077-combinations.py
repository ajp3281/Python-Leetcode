class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        combinations = []
        def backtrack(i, path):
            if len(path) == k:
                combinations.append(path.copy())
                return
            if i > n or len(path) > k:
                return

            path.append(i)
            backtrack(i + 1, path)
            path.pop()
            backtrack(i + 1, path)

        backtrack(1, [])
        return combinations


        