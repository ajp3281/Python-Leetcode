class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for i in range(numCourses):
            adj[i] = []
        for prereq in prerequisites:
            adj[prereq[1]].append(prereq[0])
            
        in_deg = [0] * numCourses 
        for edge in adj:
            for node in adj[edge]:
                in_deg[node] += 1

        
        q = deque([])
        for i in range(len(in_deg)):
            if in_deg[i] == 0:
                q.append(i)

        res = []       
        while q:
            current = q.popleft()
            res.append(current)
            
            for nei in adj[current]:
                in_deg[nei] -= 1
                if in_deg[nei] == 0:
                    q.append(nei)
        
        if len(res) == numCourses:
            return res
        else:
            return []
        
                
        
            
        