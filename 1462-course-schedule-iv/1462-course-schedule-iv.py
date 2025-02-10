class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        # topological sort?
        # how can we use it to make query time faster?
        # brute force is just bfs/dfs for each query and see if we can complete it
        # we should be flattening all prereqs..
        # can we do this with topological sort?
        # when we add to resulting array, include everything we have already visited as a prereq
        # but if its disconnected all of them might not be necessary..
        # well if its not in the list, must not be necessary
        # if it is then it is?

        in_deg = {}
        adj = {}
        for i in range(numCourses):
            in_deg[i] = 0
            adj[i] = []

        for prereq in prerequisites:
            in_deg[prereq[1]] += 1
            adj[prereq[0]].append(prereq[1])

        q = deque([])
        for node in in_deg.keys():
            if in_deg[node] == 0:
                q.append(node)

        isprereq = defaultdict(set)

        while q:
            node = q.popleft()

            for nei in adj[node]:
                in_deg[nei] -= 1
                isprereq[nei].add(node)
                for item in isprereq[node]:
                    isprereq[nei].add(item)
                if in_deg[nei] == 0:
                    q.append(nei)

        res = []
        for query in queries:
            if query[0] in isprereq[query[1]]:
                res.append(True)
            else:
                res.append(False)
        return res
