class Solution:
    def reverseBits(self, n: int) -> int:

        # 0011

        # 1100

        # keep shifting to the right and store it in a new number?

        res = 0

        for i in range(32):
            res = (n & 1) | res << 1
            n >>= 1

        return res
        