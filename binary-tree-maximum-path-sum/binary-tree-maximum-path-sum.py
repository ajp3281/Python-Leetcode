# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        
        # dfs from every node - compare result to nonlocal res val
        
        res = float("-inf")
        
        def dfs(current):
            if not current:
                return 0
            nonlocal res
            current_val = current.val 
            
            left_val = max(dfs(current.left), 0)
            right_val = max(dfs(current.right), 0)
            res = max(res, current_val + left_val + right_val)
            
            return current_val + max(left_val, right_val)
        
        dfs(root)
        return res