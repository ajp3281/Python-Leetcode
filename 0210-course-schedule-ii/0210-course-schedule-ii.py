class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # topological sort algorithm
        # if theres a cycle - we cant finish all the courses
        # start connecting nodes starting from terminal ndoes
        
        in_deg = {}
        adj = defaultdict(list)
        for i in range(numCourses):
            adj[i] = []
            in_deg[i] = 0

        for prereq in prerequisites:
            in_deg[prereq[1]] += 1
            adj[prereq[0]].append(prereq[1])

        q = deque([])
        for node in in_deg.keys():
            if in_deg[node] == 0:
                q.append(node)

        topsort = []
        while q:
            current = q.popleft()
            topsort.append(current)

            for nei in adj[current]:
                in_deg[nei] -= 1
                if in_deg[nei] == 0:
                    q.append(nei)
        
        return list(reversed(topsort)) if len(topsort) == numCourses else []