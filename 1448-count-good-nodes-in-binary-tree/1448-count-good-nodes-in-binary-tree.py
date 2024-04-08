# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def helper(current, pathmax):
            nonlocal res
            if current.val >= pathmax:
                res += 1
                pathmax = current.val
            if current.left:
                helper(current.left, pathmax)
            if current.right:
                helper(current.right, pathmax)

        helper(root,float("-inf"))
        return res