class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:

        # sort is easiest way?
        # sort - find current median and compare to k
        # check how far away k is from being median
        # res += num of operations
        if len(nums) == 1:
            return abs(k - nums[0])
        # 2 5 5 6 8
        nums.sort()

        median_idx = floor(len(nums) / 2)
        if nums[median_idx] == k:
            return 0

        res = 0
        current_median = nums[median_idx]
        if current_median > k:
            # we need to look to the left 
            # find how many elements are greater than k as they need to be made equal to k
            while nums[median_idx] > k:
                res += nums[median_idx] - k
                median_idx -= 1

        else:
            while nums[median_idx] < k:
                res += k - nums[median_idx]
                median_idx += 1
        return res

        # can we do this in o(n)?
        