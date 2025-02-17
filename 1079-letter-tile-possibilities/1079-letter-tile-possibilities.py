class Solution:
    def numTilePossibilities(self, tiles: str) -> int:

        # number of permutations?
        res = 0
        def backtrack(idx, path, used, visited):
            nonlocal res
            if str(path) not in visited:
                visited.add(str(path))
                res += 1

            if idx >= len(tiles):
                return 
            
            for i in range(len(tiles)):
                #print(res)
                if i not in used:
                    path.append(tiles[i])
                    used.add(i)
                    backtrack(idx + 1, path, used, visited)
                    path.pop()
                    used.remove(i)
            return
        
        backtrack(0, [], set(), set())
        return res - 1