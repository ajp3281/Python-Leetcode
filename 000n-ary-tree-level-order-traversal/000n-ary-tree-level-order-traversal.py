"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        q = deque([(root)])
        if not root:
            return []
        res = []
        while q:
            
            level_size = len(q)
            current_level = []
            for i in range(level_size):
                current = q.popleft()
                current_level.append(current.val)
                for nei in current.children:
                    q.append(nei)
            res.append(current_level)
        return res
                
                
            
        