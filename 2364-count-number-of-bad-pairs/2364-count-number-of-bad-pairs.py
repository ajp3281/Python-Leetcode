class Solution:
    def countBadPairs(self, nums: List[int]) -> int:

        # prefix sum / hashmap
        # iterate thru array
        # as we go through - check count of nums[j]-nums[i]
        # if we check every idx as we iterate - it will still be o(n^2) worst case
        # we should be able to count prev iterations if we increase by 1?
        # num should increase by 1 every idx.. how can we avoid checking multiple times from each idx

        # check prev occurences of good pairs.. if current idx is good w prev - must be good with rest
        # nums[i] - i = nums[j] - j
        # count number of pairs
        # subtract that by total # of pairs

        hashmap = defaultdict(int)
        for i in range(len(nums)):
            hashmap[nums[i] - i] += 1

        # formula to calculate number of pairs:
        # ((n-1) * n)/2?

        # 1,2 1,3 1,4 1,5
        # 2,3 2,4, 2,5
        # 3,4 3,5
        # 4,5

        # if it was just 3
        # 1,2,3
        # 1,2 1,3
        # 2,3
        pairs = 0
        length = len(nums)
        totalpairs = ((length - 1) * length) // 2
        for key in hashmap.keys():
            pairs += ((hashmap[key] - 1) * hashmap[key]) // 2

        
        return totalpairs - pairs




            