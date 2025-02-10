class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:

        # path cost *= edge
        # max heap as we can be greedy bc probability can't go up
        
        adj = defaultdict(list)
        for i, edge in enumerate(edges):
            adj[edge[0]].append((edge[1], succProb[i]))
            adj[edge[1]].append((edge[0], succProb[i]))
        
        heap = [(-1, start_node)]
        visited = set()
        while heap:

            prob, current = heapq.heappop(heap)

            if current in visited:
                continue

            visited.add(current)
            if current == end_node:
                return -prob

            for nei, neiprob in adj[current]:
                heapq.heappush(heap, (prob * neiprob, nei))

        return 0

        