class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def backtrack(index):
            
            if index == len(nums):
                res.append(subset.copy())
                return
                
            subset.append(nums[index])
            backtrack(index+1)
            subset.pop()
            backtrack(index+1)
            
        backtrack(0)
        return res
            
            