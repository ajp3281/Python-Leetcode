# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return (0,True)
            
            left,checkleft = dfs(node.left)
            right,checkright = dfs(node.right)
            
            
            if abs(left - right) > 1:
                checkleft = False
                checkright = False
              
            if not checkleft or not checkright:
                checkleft = False
                checkright = False
            
                
            return (max(left,right)+1,checkleft)
            
            
            
        res,booleann = dfs(root)
        return booleann
            
            
            
            
        