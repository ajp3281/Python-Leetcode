class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # find pivot index, min is idx + 1?
        # how to find pivot using binary search?
        # we know we will have 2 sorted arrays
        # we know pivot is maximum val

        # if mid > right - pivot must be to the right of mid
        # else to the left or current val

        # what if pivot is before mid?

        # 6 7 0 1 2 4 5 

        left = 0
        right = len(nums)-1
        res = float("inf")

        while left <= right:
            mid = (right + left) // 2

            
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                res = min(nums[mid], res)
                right = mid - 1

        return res
        