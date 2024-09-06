class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        def maskword(word):
            
            mask = 0
            for char in word:
                pos = ord(char) - ord('a')
                mask |= (1 << pos)
            return mask
        
        bitmasks = [0] * len(words)
        lengths = [0] * len(words)
        for i, word in enumerate(words):
            bitmasks[i] = maskword(word)
            lengths[i] = len(word)
        
        ans = 0
        for i in range(len(bitmasks)):
            for j in range(i, len(bitmasks)):
                if bitmasks[i] & bitmasks[j] == 0:
                    ans = max(ans, lengths[i] * lengths[j])
        return ans
            
        