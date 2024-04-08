# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque([(root,0)])
        res = []
        while q:
            current, currentlevel = q.popleft()
            if len(q) == 0 or currentlevel != q[0][1]:
                res.append(current.val)
            if current.left:
                q.append((current.left,currentlevel+1))
            if current.right:
                q.append((current.right, currentlevel+1))
                
        return res
        