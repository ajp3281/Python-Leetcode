"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        
        # create new nodes for every old node using hashmap
        # connect edges using dfs
        old_to_new = {}
        def dfs(current):
            #if current in o
            if current.val in old_to_new:
                return old_to_new[current.val]
            
            if current.val not in old_to_new:
                old_to_new[current.val] = Node(current.val)
                
            for nei in current.neighbors:
                old_to_new[current.val].neighbors.append(dfs(nei))
                
            return old_to_new[current.val]
        if not node:
            return None
        dfs(node)
        return dfs(node)
       