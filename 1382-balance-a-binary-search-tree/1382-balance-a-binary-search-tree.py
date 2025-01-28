# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # brute force/first idea is to iterate - store nodes, new root is median
        # build tree back 

        # do preorder traversal to store nodes

        vals = []
        def dfs(current):
            if not current:
                return
            dfs(current.left)
            vals.append(current.val)
            dfs(current.right)

        dfs(root)

        def build_tree(nodes):
            if not nodes:
                return None
            midpoint = len(nodes)//2
            new_root = TreeNode(nodes[midpoint])

            new_root.left = build_tree(nodes[:midpoint])
            new_root.right = build_tree(nodes[midpoint+1:])

            return new_root
        
        res = build_tree(vals)
        return res
        
