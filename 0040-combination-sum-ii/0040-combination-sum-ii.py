class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def helper(index, path, current):
            if current == target:
                res.append(path.copy())
                return
            
            if current > target or index >= len(candidates):
                return
            
        
            # take
            path.append(candidates[index])
            helper(index + 1, path, current + candidates[index])
            
            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1
            path.pop()
            helper(index + 1, path, current)
            
            
            
        
        candidates.sort()
        res = []
        helper(0, [], 0)
        return res