# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        res = []
        # backtracking + dfs
        # base case is if we hit leaf nodes
        def dfs(current, current_sum,path):
            path.append(current.val)
            if not current.left and not current.right:
                if current_sum + current.val == targetSum:
                    res.append(path.copy())
                else:
                    return
            if current.left:
                dfs(current.left, current_sum + current.val, path)
                path.pop()
            if current.right:
                dfs(current.right, current_sum + current.val, path)
                path.pop()

        dfs(root, 0, [])
        return res


        