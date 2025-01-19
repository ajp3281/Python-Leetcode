class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        # bit manipulation
        # go one bit at a time
        res = 0
        carry = 0
        print(bin(a), bin(b))
        for i in range(32):
            a_bit, b_bit = (a >> i) & 1, (b >> i) & 1
            sum_bit = a_bit + b_bit + carry
            if sum_bit >= 2:
                sum_bit -= 2
                carry = 1
            else:
                carry = 0
            res |= (sum_bit << i)

        if res & (1 << 31):  # If the 32nd bit is set (negative number)
            res -= (1 << 32)
        # 10100
        # 11110
        # 100010
        print(bin(res))
        return int(bin(res),2)
