class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
            
        print(adj)
        # from any node, longest path is left_height + right_height 
        # dfs to check every node
        # bottom up to pass heights?
        
        # 10
#        1
    #0   2   4
    #.   3.  5
    
        def bfs(start_node):
            visited = set()
            q = deque([(start_node, 0)])
            max_dist = float("-inf")
            while q:
                
                current, dist = q.popleft()
                visited.add(current)
                if dist > max_dist:
                    max_dist = dist
                    furthest_node = current
                for nei in adj[current]:
                    if nei not in visited:
                        q.append((nei, dist + 1))
                        
            return furthest_node, max_dist
        
        furthest_node, max_dist = bfs(1)
        print(bfs(0))
        print(bfs(furthest_node))
        return bfs(furthest_node)[1]
                
                        
            
    
    
        
        
        
        
        