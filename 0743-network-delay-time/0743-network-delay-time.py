class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        # djikstras, see how long it takes to visit every node
        # keep track of costs and return max 
        adj = defaultdict(list)
        costs = defaultdict(int)
        for time in times:
            adj[time[0]].append((time[1], time[2]))
        
        heap = [(0,0,k)]
        heapq.heapify(heap)

        # how to avoid adding
        while heap:
            current_cost, dist, node = heapq.heappop(heap)

            costs[node] = current_cost

            for nei, nei_cost in adj[node]:
                new_cost = current_cost + nei_cost
                if nei not in costs or new_cost < costs[nei]:
                    heapq.heappush(heap,(new_cost, dist + 1, nei))

        if len(costs) != n:
            return -1
        return max(costs.values())


