class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = defaultdict(list)
        
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        
        '''
        if source == destination:
            return True
        if destination not in adj:
            return False
        '''
            
        #print(adj[source])
            
        q = deque([source])
        visited = set()
        while q:
            current = q.popleft()
            
            if current == destination:
                return True
            visited.add(current)
            for nei in adj[current]:
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)
                
        return False