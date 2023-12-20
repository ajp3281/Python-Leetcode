# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(a,b):
            if not a and not b:
                return True
            if not a and b or a and not b:
                return False
            if a.left and not b.left or b.left and not a.left:
                return False
            elif a.right and not b.right or b.right and not a.right:
                return False
            elif a.val != b.val:
                return False
            if dfs(a.left,b.left) and dfs(a.right,b.right):
                return True
            else:
                return False
            
        
        return dfs(p,q)
            
        