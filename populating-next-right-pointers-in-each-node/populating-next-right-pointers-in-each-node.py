"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # at every lvl - every node should point to last lvl in node
        q = deque([root])
        if not root:
            return None

        while q:
            
            level_size = len(q)
            for i in range(level_size):
                current = q.popleft()
                
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)

                if i >= level_size-1:
                    current.next = None
                else:
                    current.next = q[0]

            

            
                
        return root
        