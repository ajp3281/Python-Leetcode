class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        
        # dp - take or skip
        
        def helper(left, right, visited):
            
            if right == len(s):
                return 0
            
            current_str = s[left:right+1]
            take = 0
            if current_str not in visited:
                visited.add(current_str)
                take = 1 + helper(right + 1, right + 1, visited)
                visited.remove(current_str)
                
            skip = helper(left, right + 1, visited)
            return max(take,skip)
        
        return helper(0,0,set())
                
            
        