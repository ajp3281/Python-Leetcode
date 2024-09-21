class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
 
        
        q = deque([(0, [0])])
        visited = set([0])
        res = []
        while q:
            print(q[0])
            current, path = q.popleft()
            if current == len(graph)-1:
                res.append(path)
            for nei in graph[current]:
                visited.add(nei)
                q.append((nei, path + [nei]))
                
        return res