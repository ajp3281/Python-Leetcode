class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        myMap = defaultdict(int)
        
        for num in nums:
            myMap[num] += 1
         
        res = 0
        for num in nums:
            longestsequence = 1
            curr = num
            if curr-1 not in myMap:
                while curr+1 in myMap:
                    longestsequence += 1
                    curr += 1
                res = max(res,longestsequence)
                
                
        return res
        