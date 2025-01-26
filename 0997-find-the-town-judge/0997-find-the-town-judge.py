class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        # count in_deg and make sure no outgoing edges from target
        in_deg = {}
        adj = {}
        for i in range(1, n+1):
            adj[i] = 0
            in_deg[i] = 0

        for a,b in trust:
            adj[a] += 1
            in_deg[b] += 1

        for i in range(1, n + 1):
            if adj[i] == 0 and in_deg[i] == n-1:
                return i
        return -1

        