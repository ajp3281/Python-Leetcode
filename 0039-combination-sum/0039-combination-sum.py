class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 
        def backtrack(combination, target, candidates, start_index):
            if sum(combination) == target:
                res.append(combination.copy())
            if sum(combination) > target:
                return
            
            for i in range(start_index, len(candidates)):
                combination.append(candidates[i])
                backtrack(combination,target,candidates,i)
                combination.pop()
            
            
        
        res = []
        backtrack([], target, candidates, 0)
        return res
            
        