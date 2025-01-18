# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        # dfs to find target value
        # if value is less - go left, else go right - return if equal 
        # if at null node return null
        # make sure to pass back return values through dfs

        def dfs(node):
            if not node:
                return None
            if node.val == val:
                return node
            if val < node.val:
                return dfs(node.left)
            elif val > node.val:
                return dfs(node.right)

        return dfs(root)
        