class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def helper(idx, path):
            if len(path) == len(nums):
                res.append(path.copy())
                return

            # num needs to be placed at every idx
            for i in range(len(nums)):
                if nums[i] not in path:
                    path.append(nums[i])
                    helper(i + 1, path)
                    path.pop()


            return 

        res = [] 
        helper(0, [])
        return res

        