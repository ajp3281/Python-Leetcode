class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        myMap = defaultdict(int)
        for char in s:
            myMap[char] += 1
        for char in t:
            myMap[char] -= 1
        for char in myMap:
            if myMap[char] != 0:
                return False
        return True
        
        