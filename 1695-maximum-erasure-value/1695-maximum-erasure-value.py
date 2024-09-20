class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        
        # max sum of unique subarray
        # always take if its not in visited
        # how to handle left/right ptr if it is in visited?
        # move up left until doesnt match with right ptr
        
        #    l          r
        # 5, 2, 1, 7, 2, 5, 2, 1, 2, 5
        l = 0
        maxsum = 0
        visited = set()
        current_sum = 0
        for r in range(len(nums)):
            if nums[r] not in visited:
                current_sum += nums[r]
                visited.add(nums[r])
            else:
                while nums[l] != nums[r]:
                    visited.remove(nums[l])
                    current_sum -= nums[l]
                    l += 1
                visited.remove(nums[l])
                current_sum -= nums[l]
                l += 1
                visited.add(nums[r])
                current_sum += nums[r]
            maxsum = max(maxsum, current_sum)
        return maxsum
                    
            
        