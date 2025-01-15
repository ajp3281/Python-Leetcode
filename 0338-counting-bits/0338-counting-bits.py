class Solution:
    def countBits(self, n: int) -> List[int]:
        
        def countBit(n):

            mask = 1
            res = 0
            for i in range(32):
                if (n & mask) == 1:
                    res += 1
                n >>= 1
            return res

        arr = []
        for i in range(n+1):
            arr.append(countBit(i))

        return arr