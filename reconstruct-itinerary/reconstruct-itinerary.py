class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        # dfs from JFK
        # jump to smallest lexicographical neighbor every time
        # how to avoid cycles?
        # pop edges as we go?
        
        adj = {}
        for ticket in tickets:
            if ticket[0] in adj: 
                adj[ticket[0]].append(ticket[1])
            else:
                adj[ticket[0]] = [ticket[1]]
            if ticket[1] not in adj:
                adj[ticket[1]] = []
        
        for node in adj:
            adj[node] = sorted(adj[node], reverse=True)
            
        print(adj)
        res = []
        def dfs(current, path):
            nonlocal res
            #print(current, path)
            print(current, path)
            '''
            if len(adj[current]) == 0:
                path.append(current)
                res = path.copy()
                return
            '''
            
            while len(adj[current]) > 0:
                next_nei = adj[current].pop()
                dfs(next_nei, path + [current])
            res.append(current)
            return

                
                
        dfs("JFK", [])    
        return res[::-1]
        
        