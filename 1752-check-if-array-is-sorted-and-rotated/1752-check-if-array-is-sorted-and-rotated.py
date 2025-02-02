class Solution:
    def check(self, nums: List[int]) -> bool:
        
        # find minimum val - make sure its increase to the right and up to it

        min_idx = 0
        min_num = float("inf")
        for i in range(1,len(nums)):
            if nums[i-1] > nums[i]:
                min_num = nums[i]
                min_idx = i

        sorted_arr = []
        for i in range(min_idx, len(nums)):
            sorted_arr.append(nums[i])

        for i in range(min_idx):
            sorted_arr.append(nums[i])

        for i in range(1,len(sorted_arr)):
            if sorted_arr[i] < sorted_arr[i-1]:
                return False
        return True