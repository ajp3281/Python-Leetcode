# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # this is bottom up 
        # if we know left subtree and rightsubtree are symmetric, then root is fine
        # how to check if left and right subtree are equal?
        # first check roots = should be equal
        # then flip left and right children
        
        # dfs w 2 parameters
        # if not root1 and not root2 : return True
        # if root1.val != rootval : return False
        # return dfs(root1.left, root2.right) and dfs(root1.right, root2.left)
        
        def dfs(root1, root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            if root1.val != root2.val:
                return False
            swap_children_1 = dfs(root1.left, root2.right)
            swap_children_2 = dfs(root2.right, root1.left)
            return swap_children_1 and swap_children_2
        
        return dfs(root,root)
            
        
        
        