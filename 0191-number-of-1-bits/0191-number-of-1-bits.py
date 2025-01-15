class Solution:
    def hammingWeight(self, n: int) -> int:
        mask = 1
        res = 0
        for i in range(32):
            if (n & mask) == 1:
                res += 1
            n >>= 1
        return res 
        