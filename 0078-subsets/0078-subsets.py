class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def helper(index, current):
            if index >= len(nums):
                res.append(current.copy())
                return
                
            # take 
            current.append(nums[index])
            helper(index + 1, current)
            # skip
            current.pop()
            helper(index + 1, current)
            
            
        res = []
        helper(0, [])
        return res