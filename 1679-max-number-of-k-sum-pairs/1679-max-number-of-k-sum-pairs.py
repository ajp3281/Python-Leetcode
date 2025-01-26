class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        # counter hashmap - remove complements + anything with count divisible by 2

        counter = Counter(nums)
        res = 0
        for num in counter.keys():
            complement = k - num
            if complement in counter:

                max_removals = min(counter[num], counter[complement])
                res += max_removals

        return res // 2