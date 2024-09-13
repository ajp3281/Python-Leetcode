# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(current):
            if not current:
                return
            dfs(current.left)
            dfs(current.right)
            res.append(current.val)
        dfs(root)
        return res
    
        