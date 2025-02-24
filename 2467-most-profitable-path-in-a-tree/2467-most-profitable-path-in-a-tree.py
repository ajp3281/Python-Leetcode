class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        # two traversals
        # dfs?
        adj = defaultdict(list)
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        # two traversals - one for bob and one for alice
        # need to keep track of when bob visits as well
        # we need dfs for bob
        visited = None
        def dfs(prev, node,path):
            nonlocal visited
            if node == 0:
                visited = path.copy()
                return
            for nei in adj[node]:
                if nei != prev:
                    path.append(nei)
                    dfs(node, nei, path)
                    path.pop()

            return

        dfs(None, bob, [bob])
        '''
        visited = []
        q = deque([(None,bob,[])])
        time = 0
        while q:
            prev, current, path = q.popleft()
            path.append(current)
            visited.append(current)
            if current == 0:
                target_path = path.copy()
            for nei in adj[current]:
                if nei != prev:
                    q.append((current, nei, path))
        '''


        q = deque([(None,0,0,0)])
        bob_visited = {}
        for i in range(len(visited)):
            bob_visited[visited[i]] = i 
        time = 0
        res = float("-inf")
        while q:
            #print(q)
            prev, current, cost, cur_time = q.popleft()
            if current in bob_visited:
                if cur_time < bob_visited[current]:
                    cost += amount[current]
                elif cur_time == bob_visited[current]:
                    cost += amount[current]//2
                else:
                    cost += 0
            else:
                cost += amount[current]

            #print(current, cost)
            # how to return early if at leaf node?
            if len(adj[current]) == 1 and current != 0:
                res = max(res, cost)
            else:
                for nei in adj[current]:
                    if nei != prev:
                        q.append((current, nei, cost, cur_time + 1))

        return res