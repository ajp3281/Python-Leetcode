class Solution:
    def minimumSteps(self, s: str) -> int:
        
        # add distance for every left ball from right?
        # keep track of how many we have seen as that affects distance?
        # need to go from right to left 
        count = 0
        left = len(s)-1
        right = len(s)-1
        res = 0
        
        while left >= 0:
            print(left, right)
            if s[left] == "1":
                res += right - left
                right -= 1
            left -= 1
        return res
                
            
            
                
                
        return res
        