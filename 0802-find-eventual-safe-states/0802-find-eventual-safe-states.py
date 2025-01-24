class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        # dfs to determine cycles
        # visited + visiting sets
        # mark terminal nodes as safe
        # if current node has a nonsafe neighbor
        # everything in current path is not safe

        def dfs(i):
            if len(graph[i]) == 0:
                isSafe[i] = True
                visited.add(i)
                return isSafe[i]

            if i in isSafe:
                return isSafe[i]
            

            isSafe[i] = False
            for nei in graph[i]:
                if not dfs(nei):
                    isSafe[i] = False
                    return isSafe[i]
            visited.add(i)
            isSafe[i] = True
            return isSafe[i]

        isSafe = {}
        visited = set()
        res = []
        for i in range(len(graph)):
            if dfs(i):
                res.append(i)
        
        return res
        