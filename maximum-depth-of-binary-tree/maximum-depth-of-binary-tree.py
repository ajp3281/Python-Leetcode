# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        ans = 0
        def dfs(current, depth):
            nonlocal ans
            if not current:
                return 
            if not current.left and not current.right:
                ans = max(ans, depth)
                return 0
            dfs(current.left, depth + 1)
            dfs(current.right, depth + 1)
            
        dfs(root,1)
        return ans