# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        depth = 0
        
        def dfs(root):
            depth = 0
            if not root.left and not root.right:
                return 1
            
            if root.left and root.right:
                depth = max(dfs(root.right)+1,dfs(root.left)+1)
                
            elif root.left:
                depth = max(depth, dfs(root.left)+1)
                
            elif root.right:
                depth = max(depth, dfs(root.right)+1)
            
            
            return depth
        
        if not root:
            return 0
        
        depth = dfs(root)
        
        return depth
    
        