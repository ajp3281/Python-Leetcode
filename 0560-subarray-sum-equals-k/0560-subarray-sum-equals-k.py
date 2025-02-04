class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        # prefix array 
        # if prefix[i] - k in hashmap - increase res by that count
        # store prefix[i]

        prefix = []
        counts = {}
        res = 0
        for r in range(len(nums)):
            if r == 0:
                prefix.append(nums[r])
            else:
                prefix.append(prefix[-1] + nums[r])

            remainder = prefix[-1] - k
            if remainder in counts:
                res += counts[remainder]
                
            counts[prefix[-1]] = counts.get(prefix[-1], 0) + 1

            if prefix[-1] == k:
                res += 1
            

        return res


        
        