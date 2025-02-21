# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.visited = set()
        # recursively iterate through nodes
        q = deque([(TreeNode(0), root)])
        while q:
            safe, contaminated = q.popleft()
            self.visited.add(safe.val)
            if contaminated.left:
                safe.left = TreeNode(safe.val * 2 + 1)
                q.append((safe.left, contaminated.left))
            if contaminated.right:
                safe.right = TreeNode(safe.val * 2 + 2)
                q.append((safe.right, contaminated.right))
        

    def find(self, target: int) -> bool:
        return target in self.visited


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)