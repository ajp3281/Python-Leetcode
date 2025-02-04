class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixarr = [nums[0]]
        for i in range(1,len(nums)):
            self.prefixarr.append(self.prefixarr[-1] + nums[i])
        
    # -2 -2 1 -4 -2 -3
    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefixarr[right]
        return self.prefixarr[right] - self.prefixarr[left-1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)