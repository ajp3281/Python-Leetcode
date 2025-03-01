class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        for i in range(len(nums)-1):
            if nums[i] == nums[i + 1]:
                nums[i+1] = 0
                nums[i] *= 2 


        res = []
        zerocount = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zerocount += 1
            else:
                res.append(nums[i])

        for i in range(zerocount):
            res.append(0)
        return res
        
        