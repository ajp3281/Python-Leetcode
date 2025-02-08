class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = defaultdict(list)

        for time in times:
            adj[time[0]].append((time[2],time[1]))

        heap = [(0, k)]
        heapq.heapify(heap)
        costs = {}

        max_cost = float("-inf")
        while heap:
            cur_cost, cur_node = heapq.heappop(heap)

            if cur_node in costs:
                continue

            costs[cur_node] = cur_cost
            max_cost = max(cur_cost, max_cost)

            if len(costs) == n:
                return max_cost

            for nei_cost, nei in adj[cur_node]:
                heapq.heappush(heap, (cur_cost + nei_cost, nei))

        print(costs)
        return -1