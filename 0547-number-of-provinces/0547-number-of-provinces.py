class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        
        adj = {}
        for i in range(len(isConnected)):
            adj[i] = []
            
        for i, node in enumerate(isConnected):
            current_neighbors = isConnected[i]
            for j in range(len(current_neighbors)):
                if current_neighbors[j] == 1 and j != i:
                    adj[i].append(j) 
               
        
        def dfs(current, visited):
            visited.add(current)
            for nei in adj[current]:
                if nei not in visited:
                    dfs(nei, visited)
        
        visited = set()
        res = 0
        for i in range(len(adj)):
            if i not in visited:
                res += 1
                dfs(i, visited)
        return res
            
        print(adj)