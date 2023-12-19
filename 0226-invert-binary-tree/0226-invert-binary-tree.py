# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        res = []
        
        def dfs(node):
            
            if not node:
                return
            
            if node.left and node.right:
                node.left, node.right = node.right, node.left
            
            if not node.right:
                node.right = node.left
                node.left = None
            elif not node.left:
                node.left = node.right
                node.right = None
            
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return root
        