class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:

        # topologically sort groups
        # if invalid group just change it to a random one
        # once we are at a group - check if there are no cycles within it
        # then check neighbors of that group
        group_ctr = max(group) + 1
        for i in range(n):
            if group[i] == -1:
                group[i] = group_ctr
                group_ctr += 1


        group_to_idx = defaultdict(list)
        for i in range(n):
            group_to_idx[group[i]].append(i)

        group_in_deg = defaultdict(set)
        group_dependencies = defaultdict(set)
        for i in group_to_idx.keys():
            for node in group_to_idx[i]:
                for predecessor in beforeItems[node]:
                    if group[predecessor] != group[node]:
                        group_dependencies[group[predecessor]].add(node)
                        group_in_deg[group[node]].add(group[predecessor])

        adj = defaultdict(list)
        for i in range(n):
            for node in beforeItems[i]:
                adj[node].append(i)
        '''
        print(group_to_idx)
        print(group_in_deg)
        print(group_dependencies)
        '''
        def bfs(current_group):
            if len(group_to_idx[current_group]) == 1:
                res.append(group_to_idx[current_group][0])
                return True
            q = deque([])
            in_deg = defaultdict(int)
            for node in group_to_idx[current_group]:
                for predecessor in beforeItems[node]:
                    if group[predecessor] == current_group:
                        in_deg[node] += 1
                if node not in in_deg:
                    in_deg[node] == 0
            print(in_deg)
            for node in group_to_idx[current_group]:
                if in_deg[node] == 0:
                    q.append(node)


            visitedlen = 0  
            while q:
                current = q.popleft()
                visitedlen += 1
                res.append(current)
                for nei in adj[current]:
                    in_deg[nei] -= 1
                    if in_deg[nei] == 0:
                        q.append(nei)

            return True if visitedlen == len(group_to_idx[current_group]) else False



        visited = set()
        q = deque([])
        res = []
        print(group_dependencies)
        print(group_in_deg)
        print(group_to_idx)
        for group_number in group_to_idx.keys():
            if group_number not in group_in_deg or group_in_deg[group_number] == 0:
                q.append(group_number)

        print(q)
        while q:
            current_group = q.popleft()
            visited.add(current_group)
            #print(q, res, current_group)
            if not bfs(current_group):
                print("testing", current_group)
                #print(group_to_idx[current_group])
                return []
            else:
                for nei in group_dependencies[current_group]:
                    if current_group in group_in_deg[group[nei]]:
                        group_in_deg[group[nei]].remove(current_group)
                        if len(group_in_deg[group[nei]]) == 0:
                            q.append(group[nei])

        print(visited)
        if len(visited) == len(group_to_idx.keys()):
            return res
        print(res)
        return []


        