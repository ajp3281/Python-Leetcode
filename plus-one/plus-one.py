class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # go through every number right to left, if number is less than 9, increase it
        # else arr = 1 + [[0] * length of digits]
        found = 0
        r = len(digits)-1
        while r >= 0:
            if digits[r] < 9:
                temp = r + 1
                while temp < len(digits) and digits[temp] == 9:
                    digits[temp] = 0
                    temp += 1
                digits[r] += 1
                return digits
            r -= 1
            
        '''
        for r in range(len(digits)-1, -1, -1):
            if digits[r] < 9:
                digits[r] += 1
                return digits
        '''
        
        res = [1] + ([0] * len(digits))
        return res
        '''
        1890
        189999
        190000
        190
        '''