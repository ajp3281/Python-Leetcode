class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        adj = defaultdict(list)
        
        for stone in stones:
            adj[tuple(stone)] = []
            
        for stone in stones:
            for key in adj:
                if stone[0] == key[0] or stone[1] == key[1]:
                    adj[key].append(tuple(stone))
        
        def dfs(current, visited):
            if not current:
                return 0
            res = 1
            visited.add((current))
            
            for nei in adj[current]:
                if nei not in visited:
                    res += dfs(nei,visited) 
            return res
        
        result = 0
        visited = set()
        count = 0
        for key in adj:
            if key not in visited:
                count += 1
                result += dfs(key, visited)
        return result - count