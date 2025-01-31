class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        
        def checkExpressiveness(word1, word2):
            l = 0
            r = 0

            while r < len(word2) or l < len(word1):

                if l >= len(word1) or r >= len(word2) or word2[r] != word1[l]:
                    return False
                
                start1, start2 = l, r
                while r + 1< len(word2) and word2[r] == word2[r+1]:
                    r += 1
                while l + 1 < len(word1) and word1[l] == word1[l+1]:
                    l += 1
                word2_count = r - start2 + 1
                word1_count = l - start1 + 1

                if word2_count > word1_count or (word2_count < word1_count and word1_count < 3):
                    return False
                l += 1
                r += 1

            return True
        
        res = 0
        #map_1 = Counter(s)
        for word in words:
            #map_2 = Counter(word)
            #if len(map_1.keys()) != len(map_2.keys()):
            #    continue
            res += checkExpressiveness(s, word)
        return res

        '''
        # counter for word and s
        # for key in s - check if its in word and s > word val and greater than 3
        # else go to next word

        # this doesn't take care of ordering!!!

        s_counter = Counter(s)
        res = 0
        flag = True
        for word in words:
            word_counter = Counter(word)
            for char in s_counter.keys():
                if char not in word_counter or (word_counter[char] > s_counter[char]) or (word_counter[char] < s_counter[char] and s_counter[char] < 3):
                    flag = False
                    break
            if flag:
                res += 1

        return res
        '''
            
        