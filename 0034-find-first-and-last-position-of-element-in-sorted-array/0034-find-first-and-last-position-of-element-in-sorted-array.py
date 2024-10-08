class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # can we just do 2 binary searches, one to find first index of target
        # one to find last index of target
        
        left = 0
        right = len(nums)-1
        t1,t2 = -1, -1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target and ((mid != 0 and nums[mid-1] != target) or mid == 0):
                t1 = mid
                
            if nums[mid] >= target:
                right = mid - 1
            
            if nums[mid] < target:
                left = mid + 1
        print(t1)        
        left = 0
        right = len(nums)-1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target and ((mid != len(nums)-1 and nums[mid+1] != target) or mid == len(nums)-1):
                t2 = mid
                
            if nums[mid] > target:
                right = mid - 1
            
            if nums[mid] <= target:
                left = mid + 1
        print(t2)
        return [t1,t2]