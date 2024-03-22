class Solution:
    def intToRoman(self, num: int) -> str:
        
        symbols = [("M",1000), ("CM",900), ("D",500), ("CD", 400), ("C", 100), ("XC", 90), 
                  ("L", 50), ("XL", 40), ("X",10), ("IX", 9), ("V",5), ("IV",4), ("I",1)]
        
        resultingstring = ""
        for i in range(len(symbols)):
            
            while num >= symbols[i][1]:
                num -= symbols[i][1]
                resultingstring += (symbols[i][0])
                
        return resultingstring
                
        