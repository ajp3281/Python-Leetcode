class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        if len(edges) == 0:
            return ((n - 1) * n) // 2
        adj = defaultdict(set)

        for edge in edges:
            adj[edge[0]].add(edge[1])
            adj[edge[1]].add(edge[0])


        def dfs(current):
            total_visited.add(current)
            visited.add(current)
            for nei in adj[current]:
                if nei not in visited:
                    dfs(nei)

        components = 0
        component_count = {}
        total_visited = set()
        for i in range(n):
            if i not in total_visited:
                visited = set()
                dfs(i)
                component_count[components] = len(visited)
                components += 1

        total_nodes = n
        res = 0
        singles = 0
        for key in component_count.keys():
            if component_count[key] == 1:
                singles += 1
            print(key, component_count[key])
            res += component_count[key] * (n - component_count[key])
            #res += (n - component_count[key])

        #res += (singles * (n-singles)) 
        # (8-4) + (8-2) + (8-1) + (8-1)
        return res // 2

        # union-find problem instead??
        # group by components?