# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        # easy to do bfs from node
        # but how do we get k distance going back up the tree?
        # should we just build an adj list then do bfs from target node?
        # would mean additional space - time should be 2*o(n) instead of o(n)
        # lets start with adj list
        q = deque([root])
        adj = defaultdict(list)
        while q:
            current = q.popleft()
            if current.left:
                adj[current.val].append(current.left.val)
                adj[current.left.val].append(current.val)
                q.append(current.left)
            if current.right:
                adj[current.val].append(current.right.val)
                adj[current.right.val].append(current.val)
                q.append(current.right)
                
        print(adj)
            
        q = deque([(target.val, 0)])
        visited = set()
        res = []
        while q:
            current, dist = q.popleft()
            visited.add(current)
            if dist == k:
                res.append(current)
            if dist < k:
                for nei in adj[current]:
                    if nei not in visited:
                        q.append((nei, dist + 1))
        return res