# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # bfs from root 
        # keep array containing max row vals?
        # how to keep track of index when negative?
        # hashmap instead of arr - if hashmap doesnt contain val for row or row val greater, add it
        if not root:
            return []
        q = deque([(root,0)])
        hashmap = defaultdict(int)
        min_row = float("inf")
        max_row = float("-inf")
        while q:
            current, row = q.popleft()
            
            if row < min_row:
                min_row = row
            if row > max_row:
                max_row = row
            
            if row not in hashmap:
                hashmap[row] = current.val
            elif current.val > hashmap[row]:
                hashmap[row] = current.val
            
            if current.left:
                q.append((current.left, row + 1))
            if current.right:
                q.append((current.right, row + 1))
                
        res = []
        for i in range(min_row, max_row + 1):
            res.append(hashmap[i])
        return res
                
        
        
        
        