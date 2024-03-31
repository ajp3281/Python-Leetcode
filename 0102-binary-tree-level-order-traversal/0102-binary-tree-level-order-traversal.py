# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        q = deque([(root,0)])
        res = []
        if root is None:
            return []
        while q:
            
            current, level = q.popleft()
            if level >= len(res):
                res.append([current.val])
            else:
                res[level].append(current.val)
            
            if current.left:
                q.append((current.left,level+1))
                
            if current.right:
                q.append((current.right,level+1))
                
        return res
                
        