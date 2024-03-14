class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) >= 2:
            y = max(stones)
            stones.remove(y)
            x = max(stones)


            if x == y:
                stones.remove(x)
            else:
                stones.remove(x)
                stones.append(y-x)
                
        if len(stones) == 1:
            return stones[0]
        else:
            return 0
            
        
            
        