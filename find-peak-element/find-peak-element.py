class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        
        while left < right:
            print(left, right)
            mid = (right + left) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            elif nums[mid] < nums[mid - 1]:
                right = mid - 1
            else:
                return mid
        return left
        