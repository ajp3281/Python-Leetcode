class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def canEat(piles,n,h):
            
            i = 0
            res = 0
            while i < len(piles):
                if n > piles[i]:
                    res += 1
                else:
                    res += ceil(piles[i]/n)
                i += 1
                    
            
            #print(res)
            if res <= h:
                return True
            return False
        
        l = 1
        r = max(piles)
        
        if len(piles) == 1 and h > piles[0]:
            return 1
        
        while l <= r:
            mid = (l+r)//2
            print(mid)
            
            
            if canEat(piles,mid,h) == True:
                r = mid-1
            
            elif canEat(piles,mid,h) == False:
                l = mid+1
            
        return l
    
        
        
            
            
            
            
        