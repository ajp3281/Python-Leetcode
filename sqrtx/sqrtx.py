class Solution:
    def mySqrt(self, x: int) -> int:
        
        # what is left and right boundaries?
        # find smallest number where mid * mid > x
        # 1 2 3 4 5 6 7 8 9 trying to find x = 9
        # l       m       r
        # l m    r
        #     lm  r
        left = 1
        right = x
        
        while left <= right:
            mid = (right + left) // 2
            if mid * mid == x:
                return mid
            if mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
        return left-1
                
        