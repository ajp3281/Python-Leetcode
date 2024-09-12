# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = None
        def dfs(current):
            nonlocal res
            if not current:
                return None
            
            check_left = dfs(current.left)
            check_right = dfs(current.right)
            if current == p:
                print(current.val, check_left, check_right)
            if check_left and check_right and res == None:
                res = current
            elif current == p:
                if check_left == q or check_right == q:
                    res = current
            elif current == q:
                if check_left == p or check_right == p:
                    res = current
            
            if current == p or current == q:
                return current
            elif check_left:
                return check_left
            elif check_right:
                return check_right
            return None
        
        dfs(root)
        return res
        