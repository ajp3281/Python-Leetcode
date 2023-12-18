class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 
        res = []
        subset = []
        
        def backtrack(index):
            
            if sum(subset) > target:
                return
            
            if sum(subset) == target:
                res.append(subset.copy())
                return
            
            for i in range(index,len(candidates)):
                
                subset.append(candidates[i])
                backtrack(i)
                subset.pop()
            
        backtrack(0)
        return res
            
            
        