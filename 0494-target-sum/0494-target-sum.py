class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def dfs(index, current, memo):
            
            if (index, current) in memo:
                return memo[(index, current)]
            if index == len(nums):
                if current == target:
                    memo[(index, current)] = 1
                    return 1
                memo[(index, current)] = 0
                return 0
            
            add, sub = 0, 0
            add += dfs(index + 1, current + nums[index], memo)
            sub += dfs(index + 1, current - nums[index], memo)
            
            memo[(index, current)] = add + sub
            return add + sub
        
        return dfs(0, 0, {})
        