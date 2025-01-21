class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        l = 0
        r = 0

        while l < len(word1) and r < len(word2):
            res += word1[l]
            l += 1
            res += word2[r]
            r += 1

        if l < len(word1):
            res += word1[l:]

        if r < len(word2):
            res += word2[r:]

        return res
        