class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        
        prefix = [0]
        res = 0
        evensum = 1
        oddsum = 0
        MOD = (10**9 + 7)
        for num in arr:
            prefix.append(prefix[-1] + num)

            if prefix[-1] % 2 == 0:
                evensum += 1
                res += oddsum
            if prefix[-1] % 2 != 0:
                oddsum += 1
                res += evensum

        return res % MOD
