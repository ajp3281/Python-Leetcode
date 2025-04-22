import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # boolean search to see if koko can eat all bananas at current x speed

        def canEat(current):
            piles_copy = piles.copy()
            
            cur_time = 0
            for banana in piles_copy:

                cur_time += math.ceil(banana / current)

            if cur_time <= h:
                return True
            return False


        left = 1
        right = max(piles)


        
        while left < right:

            mid = (right + left) // 2

            # we need leftmost val
            if canEat(mid):
                right = mid
            else:
                left = mid + 1

        return left
        