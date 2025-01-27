class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:

        MOD = 10**9 + 7
        prefix = [0]
        for i in range(len(nums)):
            prefix.append(prefix[-1] + nums[i])

        subarray_sums = []
        for i in range(1,len(prefix)):
            subarray_sums.append(prefix[i])
            for j in range(i+1, len(prefix)):
                subarray_sums.append(prefix[j] - prefix[i])

        subarray_sums.sort()
        prefix_subarray_sums = [0]
        for i in range(len(subarray_sums)):
            prefix_subarray_sums.append(prefix_subarray_sums[-1] + subarray_sums[i])    

        print(prefix_subarray_sums[right-1])
        print(prefix_subarray_sums[left])

        return (prefix_subarray_sums[right] - prefix_subarray_sums[left - 1]) % MOD