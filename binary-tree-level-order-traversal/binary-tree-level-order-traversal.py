# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([(root,0)])
        res = [[]]
        while q:
            current, level = q.popleft()
            print(current.val)
            if level < len(res):
                res[level].append(current.val)
            else:
                res.append([current.val])
                
            if current.left:
                q.append((current.left,level+1))
            if current.right:
                q.append((current.right,level+1))
                
        return res
            
            
            
            
            
        