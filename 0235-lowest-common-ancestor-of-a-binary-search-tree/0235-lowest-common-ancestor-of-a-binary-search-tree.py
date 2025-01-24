# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # dfs and pass results up
        # return value if we touch p or q
        # node can be descendant itself
        # if node.left == p|q and node.right vice versa then we found lca
        # base case return None
        res = None
        def dfs(node):
            nonlocal res
            if not node:
                return None
            left = dfs(node.left)
            right = dfs(node.right)
            print(node.val, left, right)
            if (left and right) or ((left or right) and (node.val == p.val or node.val == q.val)):
                res = node
            if node.val == p.val or node.val == q.val:
                return node.val
            
            return left or right
        
        dfs(root)
        return res