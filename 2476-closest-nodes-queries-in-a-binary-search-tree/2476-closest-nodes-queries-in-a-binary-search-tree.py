# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        # we should jsut be able to store and binary search instead of dfs every time
        nodes = []
        def dfs(current):
            if not current:
                return 
            dfs(current.left)
            nodes.append(current.val)
            dfs(current.right)

        dfs(root)
        # 5
        # [1, 2, 4, 6, 9, 13, 14, 15]
        def binarysearch(target):
            if target > nodes[-1]:
                return [nodes[-1], -1]
            if target < nodes[0]:
                return [-1, nodes[0]]

            l = 0
            r = len(nodes) - 1
            while l < r:
                mid = (r + l) // 2 
                if nodes[mid] == target:
                    return [target, target]
                if r - l == 1:
                    break
                if nodes[mid] < target:
                    l = mid
                else:
                    r = mid 
            
            if nodes[r] == target:
                return [nodes[r], nodes[r]]
            elif nodes[l] == target:
                return [nodes[l], nodes[l]]
            return [nodes[l], nodes[r]]

        res = []
        for query in queries:
            res.append(binarysearch(query))

        return res