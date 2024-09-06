class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        # keep takingleft string or keep taking right string 
        # keep track of prev taken?
        # take one or other if they match? 
        
        # what are base cases?
        # if left == len(s1) take rest of s2,
        # else take rest of s1
        if len(s1) + len(s2) != len(s3):
            return False 
        def helper(left, right, current, memo):
            
            if (left, right, current) in memo:
                return memo[(left, right, current)]
            
            
            if left == len(s1):
                #print(left, right, current)
                memo[(left, right, current)] = (s2[right:] == s3[current:])
                return s2[right:] == s3[current:]
            
            if right == len(s2):
                #print(left, right, current)
                memo[(left, right, current)] = (s1[left:] == s3[current:])
                return s1[left:] == s3[current:]
            
            if s3[current] != s1[left] and s3[current] != s2[right]:
                memo[(left, right, current)] = False
                return False
            
            check_left, check_right = False, False
            if s3[current] == s1[left]:
                check_left = helper(left + 1, right, current + 1, memo)
            if s3[current] == s2[right]:
                check_right = helper(left, right + 1, current + 1, memo)
            
            print(left, right, current)
            print(s1[left], s2[right], s3[current])
            memo[(left, right, current)] = check_left or check_right   
            return check_left or check_right
        
        return helper(0,0,0, {})
        
        