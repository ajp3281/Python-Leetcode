class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:

        res = []
        # gotta be a way to flatten every time to avoid recalculation
        # maybe a hashmap to store distance
        adj = defaultdict(list)
        for i in range(n-1):
            adj[i].append(i+1)

        def bfs(node):
            visited = set()
            visited.add(node)

            q = deque([(node,0)])

            while q:
                current, dist = q.popleft()

                if current == n-1:
                    return dist

                for nei in adj[current]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append((nei, dist + 1))
            return -1

        for query in queries:
            adj[query[0]].append(query[1])

            res.append(bfs(0))

        return res

                
                

        