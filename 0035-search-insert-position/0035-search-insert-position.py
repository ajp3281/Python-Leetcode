class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums)-1
        
        # 1, 3, 4, 6
        # find next smallest (return index + 1) or equal element (return index)
        # m = 3
        # target > m
        # left = mid
        # left = 4, right = 6
        # mid == 4
        # return mid
        
        while left <= right:
            mid = (left + right) // 2
            print(left, mid, right)
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
                
        return left