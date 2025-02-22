# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        # dashed line signifies current depth
        # how do we know which child goes where?
        # iterate through traversal and append to levels to start?
        levels = []
        levels2 = []
        l = 0
        r = 0
        idx = 0
        while r < len(traversal):

            if traversal[r] != '-':
                num_ptr = r
                while num_ptr+1 <= len(traversal)-1 and (traversal[num_ptr+1].isdigit()):
                    num_ptr += 1
                depth = r-l
                '''
                if len(levels) <= depth:
                    levels2.append([(int(traversal[r:num_ptr+1]), idx)])
                else:
                    print(num_ptr, traversal[num_ptr])
                    levels2[depth].append(((int(traversal[r:num_ptr+1]), idx)))
                '''
                
                levels.append((depth, traversal[r:num_ptr+1]))

                l = num_ptr + 1
                r = num_ptr + 1
                idx += 1
            else:
                r += 1
        
        #root = levels[0]
        # backtrack once we hit val that has less than what we are at
        # idx needs to continue to increase..
        # check idx?
        # we know left will always be idx + 1
        # we dont know right..
        # right should be number of nodes visited in left subtree + 1?
        print(levels2)
        print(levels)
        def dfs(idx, visited):
            if idx >= len(levels):
                return None

            depth, current = levels[idx]

            node = TreeNode(int(current))
            visited.add(node)
            if idx + 1 < len(levels) and depth + 1 == levels[idx+1][0]:
                node.left = dfs(idx + 1, visited)
            else:
                node.left = None

            after_left = len(visited)
            if after_left < len(levels) and depth + 1 == levels[after_left][0]:
                node.right = dfs(after_left, visited)
            else:
                node.right = None
            
            return node

        root = dfs(0, set())
        return root

        # 1

    #401

#349    #90
        
      #88