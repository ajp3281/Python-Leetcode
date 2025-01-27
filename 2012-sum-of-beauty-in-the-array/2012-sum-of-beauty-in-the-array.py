class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        running_max = []
        current_max = float("-inf")
        running_min = [0] * len(nums)
        current_min = float("inf")
        for i in range(len(nums)):
            current_max = max(current_max, nums[i])
            running_max.append(current_max)

        for i in range(len(nums)-1, -1, -1):
            current_min = min(nums[i], current_min)
            running_min[i] = current_min

        
        res = 0
        for i in range(1, len(nums)-1):
            if nums[i] > running_max[i-1] and nums[i] < running_min[i+1]:
                res += 2
            elif nums[i-1] < nums[i] < nums[i+1]:
                res += 1

        return res

        
        