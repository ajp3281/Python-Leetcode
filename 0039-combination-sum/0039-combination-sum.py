class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def helper(index, current, count):
            
            if count == target:
                res.append(current.copy())
                return
            
            if count > target or index >= len(candidates):
                return
            
            # repeat same number
            current.append(candidates[index])
            count += candidates[index]
            helper(index, current, count)
            # remove current and try next
            current.pop()
            count -= candidates[index]
            helper(index + 1, current, count)
        
        
        res = []
        helper(0, [], 0)
        return res