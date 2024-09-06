class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        def helper(index, current, memo):
            if (index, current) in memo:
                return memo[(index, current)]
            if current == amount:
                memo[(index, current)] = 1
                return 1
            if index >= len(coins) or current > amount:
                memo[(index, current)] = 0
                return 0
            
            take = helper(index, current + coins[index], memo)
            skip = helper(index + 1, current, memo)
            memo[(index, current)] = take + skip
            return take + skip
        
        return helper(0,0, {})
            
        