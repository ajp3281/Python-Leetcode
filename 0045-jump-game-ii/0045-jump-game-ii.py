class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        left = 0
        if nums[left] >= len(nums)-1:
            return 1
        count = 0
        while left < len(nums):
            right = nums[left] + left
            if right >= len(nums)-1:
                return count + 1
            
            take = 0
            next_left = left
            for index in range(left + 1, min(len(nums), right + 1)):
                if nums[index] + index > take:
                    take = nums[index] + index
                    next_left = index
            
            if next_left == left:
                return -1
            left = next_left
            count += 1

        return count
        