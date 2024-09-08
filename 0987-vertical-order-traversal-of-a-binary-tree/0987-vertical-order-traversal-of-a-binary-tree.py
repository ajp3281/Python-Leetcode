# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        all_nodes_map = defaultdict(list)
        min_col = float("inf")
        max_col = float("-inf")
        def dfs(current, row, col):
            nonlocal min_col
            nonlocal max_col
            all_nodes_map[col].append((row, current.val))
            if col < min_col:
                min_col = col
            if col > max_col:
                max_col = col
            
            if current.left:
                dfs(current.left, row + 1, col - 1)
            if current.right:
                dfs(current.right, row+1, col + 1)
        
        dfs(root, 0, 0)
        res = []
        for i in range(min_col, max_col + 1):
            if i in all_nodes_map:
                current_col = all_nodes_map[i]
                current_col.sort(key = lambda x:(x[0],x[1]))
                print(current_col)
                res.append([pos[1] for pos in current_col]) 
        return res
        