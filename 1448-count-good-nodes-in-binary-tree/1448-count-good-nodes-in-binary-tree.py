# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        # dfs, keep track of current path and current max val within the path
        # increase count if current val is > current max val
        res = 0
        def dfs(current, max_val):
            nonlocal res
            if current.val >= max_val:
                res += 1
                max_val = current.val 
            
            if current.left:
                dfs(current.left, max_val)
            
            if current.right:
                dfs(current.right, max_val)
                
            return
        
        dfs(root, float("-inf"))
        return res
                
            
        