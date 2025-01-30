class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:

        # first idea is brute force dp?
        # second idea is treat this like a graph
        # 2-1-3-4

        # place based on edges?
        # nodes at front and back must have only 1 edge 
        # rest will have 2 edges
        # continue to place based on head and tail

        adj = defaultdict(list)
        res = [0] * (len(adjacentPairs) + 1)

        in_deg = {}
        for pair in adjacentPairs:
            adj[pair[0]].append(pair[1])
            adj[pair[1]].append(pair[0])
            in_deg[pair[1]] = in_deg.get(pair[1], 0) + 1
            in_deg[pair[0]] = in_deg.get(pair[0], 0) + 1

        start_end = []
        for num in in_deg:
            if in_deg[num] == 1:
                start_end.append(num)

        print(start_end)

        visited = set()
        current = start_end[0]

        for i in range(len(res)):
            res[i] = current
            visited.add(current)
            for nei in adj[current]:
                if nei not in visited:
                    current = nei

        return res

        
