class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 
        res = []
        subset = []
        def backtrack(index):
            
            if sum(subset) == target:
                res.append(subset.copy())
                return
            
            if sum(subset) > target or index >= len(candidates):
                return
            
            subset.append(candidates[index-1])
            backtrack(index)
            subset.pop()
            backtrack(index+1)
            
        backtrack(0)
        return res
            
        