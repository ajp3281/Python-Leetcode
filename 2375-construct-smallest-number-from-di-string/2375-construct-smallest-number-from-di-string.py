class Solution:
    def smallestNumber(self, pattern: str) -> str:

        res = float("inf")

        def backtrack(idx, used, path):
            #print(path)
            nonlocal res
            if len(path) == len(pattern)+1:
                str_path = [str(x) for x in path]
                res = min(res, int(''.join(str_path)))
                return

            for i in range(1,10):
                if i not in used:
                    if (pattern[idx-1] == 'I' and i > path[idx-1]) or (pattern[idx-1] == 'D' and i < path[idx-1]):
                        path.append(i)
                        used.add(i)
                        backtrack(idx + 1, used, path)
                        path.pop()
                        used.remove(i)
            return

        for i in range(1,10):
            visited = set()
            visited.add(i)
            backtrack(1, visited, [i])
        return str(res)
        