class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        # 2x binary search, one for low of range and one for higher end of range
        
        def find_left():
            low = 0
            high = len(nums)-1
            
            while low <= high:
                mid = low + ((high - low)//2)
                print(low, mid, high)
                if nums[mid] == target:
                    high = mid - 1
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
                    
            return low
        
        def find_right():
            low = 0
            high = len(nums)-1
            while low <= high:
                mid = low + ((high - low) // 2)
                print(low, mid, high)
                if nums[mid] == target:
                    low = mid + 1
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            return high
        if len(nums) == 0:
            return [-1,-1]
        if find_right() < find_left():
            return [-1,-1]
        return ([find_left(), find_right()])
                
        