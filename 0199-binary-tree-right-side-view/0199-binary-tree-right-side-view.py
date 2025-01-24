# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        
        if not root:
            return []
        
        q = deque([root])
        res = []
        while q:
            current_level = len(q)
            for i in range(current_level):
                current = q.popleft()

                if i == current_level-1:
                    res.append(current.val)
                    
                if current.left:
                    q.append(current.left)
                    
                if current.right:
                    q.append(current.right)
                
            
                
        return res