# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque()
        Map = defaultdict(list)
        
        mincol = float('inf')
        maxcol = float('-inf')
        
        queue.append((root,0,0))
        
        while queue:
            current,curcol,currow = queue.popleft()
            
            if curcol > maxcol:
                maxcol = curcol
                
            if curcol < mincol:
                mincol = curcol
            
            Map[curcol].append((current.val,currow))
            
            if current.left:
                queue.append((current.left,curcol-1,currow+1))
            
            if current.right:
                queue.append((current.right,curcol+1,currow+1))
                
        
        result = []
        for i in range(mincol,maxcol+1):
            sorted_tuples = sorted(Map[i], key=lambda x: (x[1],x[0]))
            result.append([val for val,depth in sorted_tuples])
        
        return result
                
        