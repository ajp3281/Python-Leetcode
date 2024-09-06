class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        def helper(index1, index2, memo):
            if (index1, index2) in memo:
                return memo[(index1, index2)]

            if index1 >= len(text1) or index2 >= len(text2):
                memo[(index1, index2)] = 0
                return 0
            

            
            count = 0
            if text1[index1] == text2[index2]:
                #count = 1 + max(helper(index1+1, index2, memo), helper(index1, index2+1, memo))
                count = 1 + helper(index1+1, index2+1, memo)
            else:
                count = max(helper(index1+1, index2, memo), helper(index1, index2+1, memo))
            memo[(index1, index2)] = count
            return count
            
        
        return helper(0,0, {})
            
            
        