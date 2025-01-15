class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        count_ones_num2 = bin(num2).count('1')
        # count # of ones
        # minimize the # of ones
        # if not enough ones 1s start placing right to left
        
        # Initialize the result as 0
        result = 0
        
        # Add 1s from num1's bits to result
        for i in range(31, -1, -1):  # Iterate from the most significant bit
            if count_ones_num2 == 0:
                break
            if num1 & (1 << i):  # Check if the i-th bit in num1 is set
                result |= (1 << i)  # Set the i-th bit in result
                count_ones_num2 -= 1
        
        # Add remaining 1s from the lowest bits
        for i in range(32):  # Iterate from the least significant bit
            if count_ones_num2 == 0:
                break
            if not (result & (1 << i)):  # Check if the i-th bit in result is not set
                result |= (1 << i)  # Set the i-th bit in result
                count_ones_num2 -= 1
        
        return result




