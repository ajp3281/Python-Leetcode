class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:

        nums.sort()
        min_dif = float("inf")
        r = k-1
        l = 0
        while r <= len(nums)-1:
            min_dif = min(min_dif,nums[r] - nums[l])
            r += 1
            l += 1

        if min_dif == float("inf"):
            return 0
        return min_dif
        