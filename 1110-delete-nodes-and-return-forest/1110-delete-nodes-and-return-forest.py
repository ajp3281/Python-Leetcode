# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        res = []
        
        # find to_Delete nodes, append all their children into result?
        def dfs(node):
            nonlocal res
            if not node:
                return None
            print(node.val)
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            
            if node.val in to_delete:
                if node.left:
                    res.append(node.left)
                if node.right:
                    res.append(node.right)
                return None

            return node
        
        if dfs(root):
            res.append(root)
        return res
        
        