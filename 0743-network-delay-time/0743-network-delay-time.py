class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        # 1 -> 2 - > 3
        #.  1     2
        # 1 ------> 3
        #.     2
        adj = defaultdict(list)
        for time in times:
            adj[time[0]].append((time[1], time[2]))
        min_heap = [(0, k)]
        visited = {}
        
    
        heapq.heapify(min_heap)
        
        while min_heap:
            current_cost, current_var = heapq.heappop(min_heap)
            
            if current_var in visited:
                continue
            visited[current_var] = current_cost
            
            for neighbor, weight in adj[current_var]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, ((current_cost + weight), neighbor))
        

        if len(visited) != n:
            return -1
        return max(visited.values())
            
            
        