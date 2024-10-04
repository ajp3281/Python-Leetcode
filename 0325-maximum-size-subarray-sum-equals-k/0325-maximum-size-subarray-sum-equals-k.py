class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        
        # 1 0 5 3 6
        
        # build prefix arr , iterate from left to right as we do and keep track of maxlen
        
        prefix_arr = []
        #(-1 - (-1)) ==
        res = 0
        hashmap = {}
        for i in range(len(nums)):
            if i == 0:
                prefix_arr.append(nums[i])
            else:
                prefix_arr.append(nums[i] + prefix_arr[i-1])
            if prefix_arr[i] == k:
                res = max(res, i + 1)
            remainder = prefix_arr[i] - k
            if remainder in hashmap:
                res = max(res, i - hashmap[remainder])
            if prefix_arr[i] not in hashmap:
                hashmap[prefix_arr[i]] = i
            
        return res
            
        