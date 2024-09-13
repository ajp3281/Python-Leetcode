# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        # bottom up - keep propogating result up the tree
        # base case if a leaf node it is a unival tree
        # if left_subtree is univalue, right_subtree is univalue, and current.val == vals from each
        # then current subtree is univalue
        # nonlocal res to count?
        
        # pseudocode
        # def dfs(current):
        # if not current.left and not current.right:
        # return (True,None)
        
        # if left_subtree[0] and right_subtree[0]:
        #   if current.val == left_subtree[1] and current.val == left_subtree[1]:
        #       res += 1
        # elif just left or right, check if current.val == that roots val
        res = 0
        def dfs(current):
            nonlocal res
            if not current:
                return (True, None)
            if not current.left and not current.right:
                #print(current.val)
                res += 1
                return (True, current)
            

            left_subtree = dfs(current.left)
            right_subtree = dfs(current.right)
            if left_subtree[0] and right_subtree[0]:
                if left_subtree[1] and right_subtree[1]:
                    if current.val == left_subtree[1].val and current.val == right_subtree[1].val:
                        res += 1
                        return (True, current)
                elif not left_subtree[1]:
                    if current.val == right_subtree[1].val:
                        res += 1
                        return (True, current)
                else:
                    if current.val == left_subtree[1].val:
                        res += 1
                        return (True, current)
                        
            return (False, current)
        
        dfs(root)
        return res
            