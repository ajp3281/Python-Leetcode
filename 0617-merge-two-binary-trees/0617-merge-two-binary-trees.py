# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        # dfs with 2 roots at a time
        # base case is return 0
        # new root = left + right root

        def dfs(a, b):
            if not a and not b:
                return None

            root = TreeNode(0)
            if a and b:
                root.val = a.val + b.val
                root.left = dfs(a.left, b.left)
                root.right = dfs(a.right, b.right)
            elif a:
                root.val += a.val
                root.left = dfs(a.left, None)
                root.right = dfs(a.right, None)
            elif b:
                root.val += b.val
                root.left = dfs(None, b.left)
                root.right = dfs(None, b.right)

            return root

        res = dfs(root1, root2)
        return res
        