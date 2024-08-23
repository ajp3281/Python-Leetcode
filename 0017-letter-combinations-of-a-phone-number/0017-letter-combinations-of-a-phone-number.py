class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
            2: 'abc',
            3: 'def',
            4: 'ghi',
            5: 'jkl',
            6: 'mno',
            7: 'pqrs',
            8: 'tuv',
            9: 'wxyz',
        }
        def helper(index, current):
            if index >= len(digits):
                res.append(''.join(current.copy()))
                return

            print(phone[int(digits[index])])
            for i in range(len(phone[int(digits[index])])):
                current.append(phone[int(digits[index])][i])
                helper(index + 1, current)
                current.pop()
                
                
        
        res = []
        if len(digits) == 0:
            return []
        helper(0, [])
        return res
        