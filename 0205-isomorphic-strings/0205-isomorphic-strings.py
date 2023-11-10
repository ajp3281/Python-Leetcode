class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # map all the inputs in 1 hash - rerun thru string and replace - compare to string2
        # how do u keep count
        # 
        # hashmap of char and position
        # 
        
        myMap = {}
        myMap2 = {}
        for i in range(len(s)):
            if s[i] in myMap and t[i] != myMap[s[i]]:
                return False    
            myMap[s[i]] = t[i]
            if t[i] in myMap2 and s[i] != myMap2[t[i]]:
                return False
            myMap2[t[i]] = s[i]
        
            
        return True
            
        
        