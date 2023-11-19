class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        low = float("inf")
        high = 0
        maxProfit = 0
        for i,price in enumerate(prices):
            low = min(low,price)
            high = price
            maxProfit = max(maxProfit,high-low)
            
        return maxProfit
            
            
        
        
            
            
            
        