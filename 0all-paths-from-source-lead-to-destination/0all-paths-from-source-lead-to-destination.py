class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # check all paths but can have cycle, 
        # return False if we are in a cycle
        # keep track using prev?
        
        # 0 -> 1 
        
        # 0 -> 1 ->
        adj = defaultdict(list)
        
        for edge in edges:
            adj[edge[0]].append(edge[1])
            
        if destination in adj:
            return False
            
        def dfs(current, destination, prev, visited, memo):
            if current in memo:
                return memo[current]
            if current == destination:
                memo[current] = True
                return True
            if current in visited or len(adj[current]) == 0:
                memo[current] = False
                return False
            visited.add(current)
            for nei in adj[current]:
                if not dfs(nei, destination, current, visited, memo):
                    memo[current] = False
                    return False
            visited.remove(current)
            memo[current] = True
            return True
        
        return dfs(source, destination, None, set(), {})
            
            
        
        