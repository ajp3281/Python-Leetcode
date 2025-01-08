class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        # 2 for loops
        # iterate j < len(words), i < j

        def isPrefixAndSuffix(word1, word2):
            len1 = len(word1)
            if len1 > len(word2):
                return False
            print("Test",word1, word2[:len1], word2[len(word2)-len1:])
            if word1 == word2[:len1] and word1 == word2[len(word2)-len1:]:
                return True
            return False
        i = 0
        j = 1
        res = 0
        for i in range(0,len(words)):
            for j in range(i+1,len(words)):
                i_word = words[i]
                j_word = words[j]
                print(words[i], words[j])
                if isPrefixAndSuffix(words[i], words[j]):
                    res += 1
                print(i,j)
        return res

