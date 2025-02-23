# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        # recusive dfs 
        # next immediate node in preorder is left child
        # postorder everything before the node is its children

        # dry run
        # root = 1
        # root.left = dfs(preorder[idx+1], postorder[:idx])
        # root.right = dfs(preorder[idx+2], postorder[])
        # index after current in preorder is left child
        # index before current in postorder is right child
        # if we don't have both then we can't build
        
        visited = set()
        def dfs(preorder):
            if not preorder:
                return None

            current_elem = preorder[0]
            postorder_idx = postorder.index(current_elem) - 1
            #if postorder_idx == -1:
             #   return TreeNode(current_elem)
            #print(preorder, current_elem, postorder_idx)
            if postorder[postorder_idx] not in preorder or len(preorder) == 1:
                return TreeNode(current_elem)
            midpoint = preorder.index(postorder[postorder_idx])


            node = TreeNode(current_elem)


            node.left = dfs(preorder[1:midpoint])
            node.right = dfs(preorder[midpoint:])

            return node

        return dfs(preorder)
            
        
