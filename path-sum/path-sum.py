# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # this one is def top down , check val of current to targetsum when we are at leaf node
        
        if not root:
            return
        res = False
        def dfs(current, path):
            nonlocal res
            if not current.left and not current.right:
                if path + current.val == targetSum:
                    res = True
                return 
            
            if current.left:
                dfs(current.left, path + current.val)
            if current.right:
                dfs(current.right, path + current.val)

            
            return
        
        dfs(root, 0)
        return res
                