class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # bottom up solution, maybe top down starting with n//2 makes more natural sense?
        def p2(current):
            if 2**current == n:
                return True
            elif 2**current > n:
                return False
            else:
                return p2(current+1)
            
        return p2(0)