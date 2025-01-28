class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:

        # more edges a city has means it should contain more importance!

        adj = defaultdict(list)
        for road in roads:
            adj[road[0]].append(road[1])
            adj[road[1]].append(road[0])

        # how do we assign importance?
        # we need to go it based on length of adj list
        lengths = []
        print(adj)
        for node in adj.keys():
            lengths.append((len(adj[node]), node))

        print(lengths)
        lengths.sort()
        importance_map = {}
        importance = n
        for i in range(len(lengths)-1, -1, -1):
            importance_map[lengths[i][1]] = importance
            importance -= 1

        res = 0
        for road in roads:
            res += importance_map[road[0]] + importance_map[road[1]]

        return res

        
        