class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # kahns algo to build topological sort
        # first build adjacency list
        # next build array of indegrees
        # standards bfs - begin with nodes that have indeg of 0
        # once we reach nei, indeg--
        # if indeg == 0, add to queue
        # if len(visited) < numCourses, cycle was found
        
        graph = {}
        in_deg = [0] * numCourses
        
        for i in range(numCourses):
            graph[i] = []
            
        for prereq in prerequisites:
            graph[prereq[1]].append(prereq[0])
            
        for node in graph:
            for neighbors in graph[node]:
                in_deg[neighbors] += 1
        
        q = deque([])
        for i in range(numCourses):
            if in_deg[i] == 0:
                q.append(i)
                
        res = []
        while q:
            current = q.popleft()
            res.append(current)
            for nei in graph[current]:
                in_deg[nei] -= 1
                if in_deg[nei] == 0:
                    q.append(nei)
        if len(res) == numCourses:
            return res
        else:
            return []