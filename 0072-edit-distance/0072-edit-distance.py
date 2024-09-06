class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # base case - leftptr < len(word1) and rightptr == len(word2) - just add all left words in word2
        # base case - rightptr < len(word2) - remove all leftover words in word1
        def helper(left, right, memo):
            if (left,right) in memo:
                return memo[(left, right)]
            if right == len(word2):
                memo[(left, right)] = len(word1) - left
                return len(word1) - left
            
            if left == len(word1):
                memo[(left, right)] = len(word2) - right
                return len(word2) - right
            
            if word1[left] == word2[right]:
                return helper(left + 1, right + 1, memo)
            else:
                add = helper(left, right + 1, memo) + 1
                rem = helper(left + 1, right, memo) + 1
                replace = helper(left + 1, right + 1, memo) + 1
                
                memo[(left, right)] = min(add, rem, replace)
                return min(add, rem, replace)
            
        return helper(0,0, {})
            
        