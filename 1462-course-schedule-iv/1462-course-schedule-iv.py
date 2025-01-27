class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        # brute force by doing bfs/dfs from nodes
        adj = defaultdict(list)
        for prereq in prerequisites:
            adj[prereq[0]].append(prereq[1])

        def bfs(i):
            q = deque([i])
            visited = set()
            visited.add(i)
            while q:
                current = q.popleft()
                for nei in adj[current]:
                    if nei not in visited:
                        q.append(nei)
                        visited.add(nei)
            return visited

        reachable = []
        for i in range(numCourses):
            visited = bfs(i)
            reachable.append(visited)

        res = []
        for query in queries:
            if query[1] in reachable[query[0]]:
                res.append(True)
            else:
                res.append(False)
        return res

        

        
