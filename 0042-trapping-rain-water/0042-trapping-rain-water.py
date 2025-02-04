class Solution:
    def trap(self, height: List[int]) -> int:

        # rain at index = min(max of left and right) - currentidx

        max_from_left = [0] * len(height)
        max_from_right = [0] * len(height)
        for r in range(len(height)):
            if r > 0:
                max_from_left[r] = max(max_from_left[r-1], height[r])
            else:
                max_from_left[r] = height[r]

        for r in range(len(height)-1, -1, -1):
            if r < len(height)-1:
                max_from_right[r] = (max(max_from_right[r + 1], height[r]))
            else:
                max_from_right[r] = height[r]

        res = 0
        for i in range(len(height)):

            min_from_each_side = min(max_from_left[i], max_from_right[i])

            res += min_from_each_side - height[i]

        return res
        