class Solution:
    def canPartition(self, nums: List[int]) -> bool:
       # dfs find if u can build array with half sum of nums
    
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2
        
        def dfs(index, current, memo):
            if current > target:
                memo[(index, current)] = False
                return False
            
            if current == target:
                memo[(index, current)] = True
                return True
            
            if index >= len(nums):
                memo[(index, current)] = False
                return False
            
            if (index, current) in memo:
                return memo[(index, current)]
            
            include = dfs(index + 1, current + nums[index], memo)
            if include:
                memo[(index, current)] = include
                return True
            
            exclude = dfs(index + 1, current, memo)
            
            memo[(index, current)] = include or exclude
            return include or exclude
        
        return dfs(0, 0, {})
            
            