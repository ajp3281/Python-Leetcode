class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = defaultdict(list)
        

        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        
        def dfs(current, visited):
            visited.add(current)
            if current == destination:
                return True
            for nei in adj[current]:
                if nei not in visited:
                    if dfs(nei, visited):
                        return True
            return False
        
        return dfs(source, set())
            
        