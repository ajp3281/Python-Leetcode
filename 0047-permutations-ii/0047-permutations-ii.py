class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        '''
        1
        
    1,
        '''
        res = []
        def helper(index, path, visited):
            nonlocal res
            if index >= len(nums):
                if path not in res:
                    res.append(path.copy())
                return  
            for ind, num in enumerate(nums):
                if ind not in visited:
                    path.append(num)
                    visited.add(ind)
                    helper(index + 1, path, visited)
                    path.pop()
                    visited.remove(ind)
                
        helper(0, [], set())
        return res
                
        