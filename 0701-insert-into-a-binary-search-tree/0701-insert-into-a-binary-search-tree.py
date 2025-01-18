# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        # how to insert into a binary tree?
        # easiest way is to just insert at leaf node?
        # can we always insert at leaf node?
        
        # lets start with just leaf
        # how should we handle the recursion?
        # if not node, return new node with target val?
        # else continue navigating through tree?
        # in dfs - root.left = dfs(node.left), root.right = dfs(root.right)
        # return root?

        def dfs(node):
            if not node:
                return TreeNode(val)
            if val > node.val:
                node.right = dfs(node.right)
            else:
                node.left = dfs(node.left)
            return node

        return dfs(root)
        