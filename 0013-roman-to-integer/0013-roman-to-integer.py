class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        res = 0
        i = 0
        while i < len(s)-1:
            
            if symbols[s[i]] < symbols[s[i+1]]:
                res += symbols[s[i+1]] - symbols[s[i]]
                i += 1
                
            else:
                res += symbols[s[i]]
            i += 1
            print(res)
            
        
        if symbols[s[len(s)-1]] <= symbols[s[len(s)-2]]:
            res += symbols[s[len(s)-1]]
            
            
        return res
                
        